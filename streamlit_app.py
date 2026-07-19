import streamlit as st
from agent import Agent
from memory import clear_memory

st.set_page_config(
    page_title="AI Agent",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
    .stApp { background-color: #0d1117; }
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ff6b00, #ffa500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        text-align: center;
        color: #8b949e;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
    }
    .tool-badge {
        display: inline-block;
        background: #1c2333;
        border: 1px solid #30363d;
        border-radius: 20px;
        padding: 4px 12px;
        margin: 3px;
        font-size: 0.8rem;
        color: #8b949e;
    }
    .chat-user {
        background: #1f3a5f;
        border-radius: 12px 12px 2px 12px;
        padding: 10px 15px;
        margin: 8px 0;
        color: #e6edf3;
        max-width: 80%;
        margin-left: auto;
    }
    .chat-bot {
        background: #1c2333;
        border-radius: 12px 12px 12px 2px;
        padding: 10px 15px;
        margin: 8px 0;
        color: #e6edf3;
        max-width: 80%;
        border-left: 3px solid #ff6b00;
    }
    .stTextInput > div > div > input {
        background-color: #161b22 !important;
        color: #e6edf3 !important;
        border: 1px solid #30363d !important;
        border-radius: 10px !important;
    }
    .stButton > button {
        background: linear-gradient(90deg, #ff6b00, #ffa500) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🤖 AI Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Powered by Gemma 3 · OpenRouter · Free API</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-bottom: 1rem;">
    <span class="tool-badge">🧮 Calculator</span>
    <span class="tool-badge">🌤️ Weather</span>
    <span class="tool-badge">🕐 Time</span>
    <span class="tool-badge">😂 Jokes</span>
    <span class="tool-badge">💬 General Chat</span>
</div>
""", unsafe_allow_html=True)

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent" not in st.session_state:
    st.session_state.agent = Agent()

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-user">👤 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bot">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input(
            label="message",
            placeholder="Ask me anything — weather, math, jokes, or just chat...",
            label_visibility="collapsed"
        )
    with col2:
        submit = st.form_submit_button("Send →")

if submit and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        response = st.session_state.agent.run(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

st.divider()
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        clear_memory()
        st.rerun()

st.markdown("""
<div style="text-align:center; color:#30363d; font-size:0.75rem; margin-top:1rem;">
    Built with Streamlit · Gemma 3 12B · OpenRouter Free API
</div>
""", unsafe_allow_html=True)
