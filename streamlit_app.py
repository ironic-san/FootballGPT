import streamlit as st

from chatbot import FootballChatbot
from config import APP_NAME, VERSION


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="⚽",
    layout="centered"
)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "bot" not in st.session_state:
    st.session_state.bot = FootballChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("⚽ FootballGPT")

    st.caption(f"Version {VERSION}")

    st.markdown("---")

    st.subheader("🤖 Active Model")

    st.success(st.session_state.bot.current_model)

    st.caption(f"Provider: {st.session_state.bot.current_provider}")

    st.markdown("---")

    st.subheader("📖 About")

    st.markdown("""
FootballGPT is your personal AI football assistant.

It can help you with:

- ⚽ Players
- 🏆 Clubs
- 🌍 FIFA World Cup
- 🇪🇺 UEFA Competitions
- 📚 Football Rules
- 🎯 Tactics & Formations
- 📈 Player Comparisons
- 🎮 EA Sports FC / FIFA Games
""")

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown("""
✅ Conversation Memory

✅ Automatic Model Switching

✅ Multiple AI Models

✅ Streamlit Chat Interface

🔜 Football RAG

🔜 Live Football API
""")

    st.markdown("---")

    st.subheader("🔄 Model Priority")

    st.markdown("""
1️⃣ Gemini 3.1 Flash Lite

2️⃣ Gemini 2.5 Flash

3️⃣ Gemma 4 26B
""")

    st.markdown("---")

    if st.button("🗑️ New Chat", use_container_width=True):

        st.session_state.bot = FootballChatbot()

        st.session_state.messages = []

        st.rerun()

# --------------------------------------------------
# Main Page
# --------------------------------------------------

st.title("⚽ FootballGPT")

st.caption("Your Personal AI Football Assistant")

# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

prompt = st.chat_input("Ask anything about football...")

if prompt:

    # User Message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # Assistant Message

    with st.chat_message("assistant"):

        with st.spinner("⚽ FootballGPT is thinking..."):

            result = st.session_state.bot.chat(prompt)

            st.caption(
                f"🤖 {result['model']} • {result['provider']}"
            )

            st.markdown(result["answer"])

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"]
        }
    )