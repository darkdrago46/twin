"""JSON API for the portfolio's native chat box.

Reuses context.py (system prompt) and tools.py (tool calls) from the Gradio app.
Run locally:  uvicorn server:app --reload
Run on Render: uvicorn server:app --host 0.0.0.0 --port $PORT
"""
import os
import time
from collections import defaultdict, deque

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from pydantic import BaseModel, Field

from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls

load_dotenv(override=True)

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.5-flash-lite")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is missing. Set it in Render's environment variables.")

# Comma-separated list, e.g. "https://soumik.dev,https://soumik.netlify.app". "*" allows any site.
ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",") if o.strip()]

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=GOOGLE_API_KEY,
)

app = FastAPI(title="Soumik's Digital Twin API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class Turn(BaseModel):
    role: str
    content: str = Field(max_length=4000)


class ChatIn(BaseModel):
    message: str = Field(min_length=1, max_length=800)
    history: list[Turn] = Field(default_factory=list, max_length=20)


# Simple in-memory rate limit per visitor: 20 questions per 10 minutes.
HITS: dict[str, deque] = defaultdict(deque)
LIMIT, WINDOW = 20, 600


def is_limited(ip: str) -> bool:
    now = time.time()
    hits = HITS[ip]
    while hits and now - hits[0] > WINDOW:
        hits.popleft()
    if len(hits) >= LIMIT:
        return True
    hits.append(now)
    return False


@app.get("/")
@app.get("/health")
def health():
    return {"ok": True}


@app.post("/api/chat")
def chat(body: ChatIn, request: Request):
    forwarded = request.headers.get("x-forwarded-for", "").split(",")[0].strip()
    ip = forwarded or (request.client.host if request.client else "unknown")
    if is_limited(ip):
        raise HTTPException(status_code=429, detail="Rate limit reached")

    history = [
        {"role": t.role, "content": t.content}
        for t in body.history
        if t.role in ("user", "assistant")
    ][-10:]
    messages = (
        [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]
        + history
        + [{"role": "user", "content": body.message}]
    )

    try:
        for _ in range(5):  # cap tool-call loops
            response = client.chat.completions.create(
                model=MODEL_NAME, messages=messages, tools=tools
            )
            choice = response.choices[0]
            if choice.finish_reason != "tool_calls":
                return {"reply": choice.message.content or ""}
            messages.append(choice.message)
            messages.extend(handle_tool_calls(choice.message.tool_calls))
    except Exception:
        raise HTTPException(status_code=502, detail="Model request failed")

    return {"reply": "Sorry, I couldn't finish that. Please try again."}
