import os
import streamlit as st
from dotenv import load_dotenv
from utils import init_openai_client, parse_pdf, call_chat_completion
from tavily import TavilyClient
import textwrap
import time

# --- Load environment variables ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# --- Initialize clients ---
init_openai_client(api_key=OPENAI_API_KEY, api_base=OPENAI_API_BASE)
tavily_client = TavilyClient(api_key=TAVILY_API_KEY) if TAVILY_API_KEY else None

# --- Streamlit Page Setup ---
st.set_page_config(page_title="BOO Research Tool", page_icon="🧭", layout="wide")

# --- Hero Section ---
st.markdown(
    """
    <style>
    .main-title {
        font-size: 40px;
        font-weight: 800;
        color: #1E3A8A;
        text-align: center;
        margin-top: -30px;
        animation: fadein 2s ease-in-out;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #4B5563;
        margin-bottom: 30px;
    }
    @keyframes fadein {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0px); }
    }
    footer {
        text-align: center;
        font-size: 14px;
        color: #6B7280;
        margin-top: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">🧭 BOO RESEARCH TOOL</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-powered assistant for live web research + document analysis</div>',
    unsafe_allow_html=True,
)

# --- Sidebar ---
st.sidebar.markdown(
    "<h1 style='text-align:center; font-size:60px; margin-bottom:-10px;'>🧭</h1>",
    unsafe_allow_html=True
)
st.sidebar.title("🧭 BOO RESEARCH TOOL")
st.sidebar.caption("Built for researchers, data scientists & AI engineers")
st.sidebar.markdown("---")

st.sidebar.header("⚙️ Settings")
model = st.sidebar.selectbox(
    "Select a Model",
    [
        "gpt-4o",
        "mistralai/mistral-small-3.1-24b-instruct:free",
        "meta-llama/llama-4-maverick:free",
        "deepseek/deepseek-chat-v3-0324:free"
    ],
    index=0
)
temperature = st.sidebar.slider("Creativity (temperature)", 0.0, 1.5, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 64, 4096, 1024)
use_web = st.sidebar.checkbox("🌐 Include Live Web Search (Tavily)", value=True if TAVILY_API_KEY else False)
st.sidebar.markdown("---")
st.sidebar.info("💡 GPT-4o offers best reasoning accuracy; free models are good for light or fast tests.")

# --- Chat state ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Upload & context ---
with st.expander("📎 Upload Research File (PDF or TXT)"):
    uploaded = st.file_uploader("Upload File", type=["pdf", "txt"])
    pasted = st.text_area("Or paste text here", height=150)
    context_text = ""
    if uploaded:
        if uploaded.type == "application/pdf":
            context_text = parse_pdf(uploaded)
        else:
            context_text = uploaded.getvalue().decode("utf-8")
    elif pasted.strip():
        context_text = pasted.strip()

# --- Input box ---
user_input = st.text_area("💬 Ask a question or research topic", height=120)

if st.button("Send"):
    if not user_input:
        st.warning("Please enter a prompt.")
    else:
        st.session_state.history.append({"role": "user", "content": user_input})

        web_snippets = ""
        if use_web and tavily_client:
            with st.spinner("🌍 Searching the web (Tavily)..."):
                try:
                    results = tavily_client.search(user_input)
                    if "results" in results and results["results"]:
                        for r in results["results"][:5]:
                            title = r.get("title", "")
                            content = r.get("content", "")
                            link = r.get("url", "")
                            web_snippets += f"\n- **{title}**: {textwrap.shorten(content, 300)} ([source]({link}))"
                except Exception as e:
                    web_snippets = f"(Web search failed: {e})"

        with st.spinner(f"🧠 Generating response using {model}..."):
            system_prompt = (
                "You are a research assistant. Combine live web data with uploaded documents. "
                "Provide clear, verified, and structured answers. Cite sources when possible."
            )

            messages = [{"role": "system", "content": system_prompt}]
            if context_text:
                messages.append({"role": "user", "content": f"Context from uploaded text:\n{context_text[:4000]}"})
            if web_snippets:
                messages.append({"role": "user", "content": f"Relevant live web data:\n{web_snippets}"})
            for m in st.session_state.history[-4:]:
                messages.append({"role": m["role"], "content": m["content"]})

            try:
                response = call_chat_completion(messages, model, temperature, max_tokens)
                assistant_reply = response.get("text") or "No response generated."
            except Exception as e:
                st.warning(f"{model} failed — retrying with GPT-4o...")
                response = call_chat_completion(messages, "gpt-4o", temperature, max_tokens)
                assistant_reply = response.get("text") or "No response generated."

            st.session_state.history.append({"role": "assistant", "content": assistant_reply})

# --- Chat Display ---
st.markdown("---")
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 Assistant:** {msg['content']}")
        time.sleep(0.05)

# --- Footer ---
st.markdown(
    """
    <footer>Developed with ❤️ by <strong>Eng. Brian Otieno</strong> — Empowering Intelligent Research</footer>
    """,
    unsafe_allow_html=True,
)
