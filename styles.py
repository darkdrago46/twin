"""Monochrome futuristic styling for the Digital Twin Gradio app."""

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = r"""
:root {
  color-scheme: dark;
  --twin-bg: #09090c;
  --twin-glow: #171720;
  --twin-surface: rgba(22, 22, 29, .88);
  --twin-surface-2: #202029;
  --twin-border: rgba(190, 190, 210, .16);
  --twin-border-strong: rgba(205, 205, 225, .28);
  --twin-text: #f1f1f5;
  --twin-muted: #a0a0ad;
  --twin-subtle: #777783;
  --twin-accent: #d5d5df;
  --twin-accent-text: #111116;
  --twin-user: #e7e7ee;
  --twin-user-text: #15151b;
  --twin-bot: #202029;
  --twin-shadow: 0 24px 80px rgba(0,0,0,.34);
  --twin-radius: 18px;
}

body:not(.dark) {
  color-scheme: light;
  --twin-bg: #f2f2f5;
  --twin-glow: #e6e6ed;
  --twin-surface: rgba(255,255,255,.92);
  --twin-surface-2: #f0f0f4;
  --twin-border: rgba(30,30,45,.11);
  --twin-border-strong: rgba(30,30,45,.20);
  --twin-text: #17171d;
  --twin-muted: #62626e;
  --twin-subtle: #858590;
  --twin-accent: #292932;
  --twin-accent-text: #fff;
  --twin-user: #292932;
  --twin-user-text: #fff;
  --twin-bot: #f0f0f4;
  --twin-shadow: 0 20px 60px rgba(25,25,40,.08);
}

html, body, gradio-app {
  min-height: 100%;
  background:
    radial-gradient(ellipse at 80% 5%, var(--twin-glow), transparent 38%),
    var(--twin-bg) !important;
  color: var(--twin-text) !important;
}
.gradio-container {
  width: 100% !important;
  max-width: 1480px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 22px clamp(14px, 3vw, 42px) 36px !important;
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important; max-width: 100% !important; min-width: 0 !important;
}
.gradio-container * { min-width: 0; }
footer, .built-with, .show-api, .api-docs { display: none !important; }

/* Top bar */
#twin-topbar {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  margin: 0 0 16px !important;
  gap: 14px !important;
}
#twin-brand h1 {
  color: var(--twin-text) !important;
  font-size: clamp(19px, 2vw, 25px) !important;
  letter-spacing: -.045em !important;
  font-weight: 750 !important;
  margin: 0 !important;
}
#twin-brand p {
  color: var(--twin-muted) !important;
  font-size: 11px !important;
  letter-spacing: .16em !important;
  text-transform: uppercase !important;
  margin: 3px 0 0 !important;
}
#twin-theme-toggle button {
  border-radius: 999px !important;
  min-height: 38px !important;
  padding: 0 15px !important;
  background: var(--twin-surface-2) !important;
  border: 1px solid var(--twin-border-strong) !important;
  color: var(--twin-text) !important;
}

/* Main split layout */
#twin-shell {
  display: grid !important;
  grid-template-columns: minmax(285px, 350px) minmax(0, 1fr) !important;
  align-items: stretch !important;
  gap: 18px !important;
  width: 100% !important;
  min-height: min(830px, calc(100vh - 100px)) !important;
}
#twin-profile, #twin-chat-panel {
  min-width: 0 !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius) !important;
  background: var(--twin-surface) !important;
  box-shadow: var(--twin-shadow) !important;
  backdrop-filter: blur(22px);
  -webkit-backdrop-filter: blur(22px);
  overflow: hidden !important;
}
#twin-profile {
  padding: 22px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
}
#twin-chat-panel {
  padding: clamp(16px, 2.2vw, 30px) !important;
  min-height: 680px !important;
}

/* Profile image */
#twin-avatar {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  padding: 0 !important;
}
#twin-avatar img {
  width: 100% !important;
  height: 245px !important;
  object-fit: cover !important;
  object-position: center 28% !important;
  border-radius: 15px !important;
  filter: grayscale(100%) contrast(1.04);
  border: 1px solid var(--twin-border) !important;
}
#twin-profile h2, #twin-profile h3 {
  color: var(--twin-text) !important;
  letter-spacing: -.025em !important;
}
#twin-profile h2 { font-size: 27px !important; margin: 0 0 2px !important; }
#twin-profile h3 { font-size: 14px !important; margin: 10px 0 5px !important; }
#twin-profile p, #twin-profile li {
  color: var(--twin-muted) !important;
  font-size: 13px !important;
  line-height: 1.6 !important;
}
#twin-profile ul { margin-top: 4px !important; padding-left: 18px !important; }
#twin-profile hr { border-color: var(--twin-border) !important; opacity: 1 !important; }

/* Chatbot */
#twin-chatbot, .chatbot, .chatbot.block {
  min-height: 500px !important;
  background: transparent !important;
  border: 0 !important;
  border-radius: 15px !important;
  box-shadow: none !important;
}
.chatbot > .block-label, .chatbot > label, .chatbot .label-wrap,
.chatbot .block-label, .chatbot > .label-container { display: none !important; }
.chatbot .placeholder, .chatbot .placeholder * { color: var(--twin-muted) !important; }

.message-row, .message-row > div, .message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important; border: 0 !important; box-shadow: none !important;
}
.message-row .message, .message-row .message-bubble, .message-row .bubble {
  border: 1px solid var(--twin-border) !important;
  box-shadow: none !important;
  border-radius: 15px !important;
  padding: 11px 15px !important;
  font-size: 14px !important;
  line-height: 1.65 !important;
}
.message-row.user-row .message, .message-row.user-row .message-bubble,
.message-row.user-row .bubble, .message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: var(--twin-user) !important;
  color: var(--twin-user-text) !important;
  border-color: transparent !important;
}
.message-row.bot-row .message, .message-row.bot-row .message-bubble,
.message-row.bot-row .bubble, .message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble,
.message-row[data-role="assistant"] .bubble {
  background: var(--twin-bot) !important;
  color: var(--twin-text) !important;
  border-color: var(--twin-border) !important;
}
.message-row .message p, .message-row .message-bubble p,
.message-row .bubble p, .message-row .prose p {
  color: inherit !important; font-size: 14px !important;
  line-height: 1.65 !important; margin: 0 0 9px !important;
}
.message-row .message p:last-child, .message-row .message-bubble p:last-child,
.message-row .bubble p:last-child, .message-row .prose p:last-child { margin-bottom: 0 !important; }
.message-row .message a, .message-row .message-bubble a {
  color: inherit !important; text-decoration: underline; text-underline-offset: 3px;
}

/* Textbox and buttons */
.input-row, .gr-input-row, .chat-input-row, form[class*="input"] {
  align-items: stretch !important; gap: 10px !important;
}
textarea, input[type="text"] {
  background: var(--twin-surface-2) !important;
  border: 1px solid var(--twin-border-strong) !important;
  border-radius: 14px !important;
  color: var(--twin-text) !important;
  font: 14px/1.5 Inter, -apple-system, BlinkMacSystemFont, sans-serif !important;
  padding: 13px 16px !important; min-height: 50px !important;
  box-shadow: none !important;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--twin-muted) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px rgba(150,150,170,.12) !important;
}
textarea::placeholder, input::placeholder { color: var(--twin-subtle) !important; }
button {
  border-radius: 12px !important;
  border: 1px solid var(--twin-border-strong) !important;
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
  font: 600 13px Inter, -apple-system, BlinkMacSystemFont, sans-serif !important;
  letter-spacing: 0 !important; text-transform: none !important;
  min-height: 44px !important; padding: 0 16px !important;
  transition: background .18s ease, border-color .18s ease, transform .18s ease !important;
}
button:hover { border-color: var(--twin-muted) !important; transform: translateY(-1px); }
button.primary, button[variant="primary"], button.submit,
button.submit-button, .submit-button, button.lg.primary {
  background: var(--twin-accent) !important;
  border: 1px solid var(--twin-accent) !important;
  color: var(--twin-accent-text) !important; font-weight: 700 !important;
}
button.primary:hover, button.submit:hover, button.submit-button:hover,
.submit-button:hover, button.lg.primary:hover { filter: brightness(1.08); }

/* Suggested prompts */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important; padding: 0 !important; margin-top: 14px !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }
.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-surface-2) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important; border-radius: 12px !important;
  text-transform: none !important; letter-spacing: 0 !important;
  font: 500 13px Inter, -apple-system, BlinkMacSystemFont, sans-serif !important;
  padding: 12px 14px !important; text-align: left !important; min-height: 0 !important;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--twin-border-strong) !important;
  background: var(--twin-surface) !important;
}

/* Mobile */
@media (max-width: 760px) {
  .gradio-container { padding: 16px 12px 26px !important; }
  #twin-shell { display: flex !important; flex-direction: column !important; gap: 12px !important; }
  #twin-profile, #twin-chat-panel { width: 100% !important; border-radius: 15px !important; }
  #twin-profile { padding: 17px !important; }
  #twin-chat-panel { padding: 13px !important; min-height: 600px !important; }
  #twin-avatar img { height: 280px !important; }
  #twin-chatbot, .chatbot, .chatbot.block { min-height: 430px !important; }
}

::selection { background: var(--twin-accent); color: var(--twin-accent-text); }
::-webkit-scrollbar { width: 9px; height: 9px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--twin-border-strong); border-radius: 99px; }
"""

JS = r"""
() => {
  document.title = "Soumik Rakshit | Digital Twin";
  document.body.classList.add("dark");

  const focusInput = () => {
    const areas = document.querySelectorAll("textarea");
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 350);

  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = "1";
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ["disabled", "readonly"] });
  };

  const scan = () => document.querySelectorAll("textarea").forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""
