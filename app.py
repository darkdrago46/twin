from pathlib import Path
import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES

load_dotenv(override=True)

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.5-flash-lite")
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is missing. Add it to your .env file.")

client = OpenAI(base_url=GEMINI_BASE_URL, api_key=GOOGLE_API_KEY)
SYSTEM_MESSAGES = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]

PROFILE_IMAGE = Path(__file__).parent / "assets" / "profile.png"


def chat(message, history):
    """ChatInterface callback. History uses Gradio's messages format."""
    messages = SYSTEM_MESSAGES + (history or []) + [
        {"role": "user", "content": message}
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
    )

    while response.choices[0].finish_reason == "tool_calls":
        assistant_message = response.choices[0].message
        tool_results = handle_tool_calls(assistant_message.tool_calls)
        messages.append(assistant_message)
        messages.extend(tool_results)

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
        )

    return response.choices[0].message.content


def toggle_theme():
    # The browser-side JS toggles the body class; this callback keeps
    # the Gradio event wired without changing the chat state.
    return None


with gr.Blocks(
    title="Soumik Rakshit | Digital Twin",
) as demo:
    with gr.Row(elem_id="twin-topbar"):
        gr.Markdown(
            "### SOUMIK RAKSHIT\n\nDIGITAL TWIN / SOFTWARE ENGINEER",
            elem_id="twin-brand",
        )
        theme_button = gr.Button("☼  /  ☾", elem_id="twin-theme-toggle")

    # CSS turns this row into the two-column profile + chat composition.
    with gr.Row(elem_id="twin-shell"):
        with gr.Column(elem_id="twin-profile", scale=1, min_width=270):
            gr.Image(
                value=str(PROFILE_IMAGE),
                label=None,
                show_label=False,
                interactive=False,
                container=False,
                elem_id="twin-avatar",
            )
            gr.Markdown(
                """
## Soumik Rakshit
**Software Engineer · Citi**

Building scalable backend systems, one commit at a time.

---

### About me
Software Engineer at Citi, Chennai, focused on backend engineering,
distributed systems and building reliable applications.

### Focus areas
`Backend` · `Distributed Systems` · `Payments`

### Technical toolkit
Java · Spring Boot · Kafka · Spark · Angular · SQL · Docker · Jenkins

---

### Highlights
- Rates Risk Intraday UI used by traders
- IBM Grid to cloud migration
- 96% CI build-time improvement
- Significantly faster Spark-based payment processing

### Recognition
- Citi Q2 2025 Gold Award
- Star Performer (twice)
- Best Paper — IEEE ICNWC 2023
                """
            )

        with gr.Column(elem_id="twin-chat-panel", scale=3, min_width=420):
            gr.Markdown(
                """
## Hey there. 👋
I'm Soumik's Digital Twin. Ask me about my background, technical skills,
projects, or career journey.
                """
            )
            gr.ChatInterface(
                fn=chat,
                chatbot=gr.Chatbot(
                    show_label=False,
                    height=510,
                    elem_id="twin-chatbot",
                ),
                textbox=gr.Textbox(
                    placeholder="Ask me anything...",
                    show_label=False,
                    container=False,
                ),
                examples=EXAMPLES,
                title=None,
                description=None,
                cache_examples=False,
            )

    theme_button.click(
        fn=toggle_theme,
        inputs=None,
        outputs=None,
        js="() => { document.body.classList.toggle('dark'); return []; }",
    )


if __name__ == "__main__":
    demo.launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base()
    )
