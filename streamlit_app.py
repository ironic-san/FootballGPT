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
FootballGPT combines **Gemini AI** with a **Retrieval-Augmented Generation (RAG)** system to answer football questions using official football documents.

### It can answer questions about:

- ⚽ Players
- 🏆 Clubs
- 🌍 FIFA World Cup
- 🇪🇺 UEFA Competitions
- 📚 Laws of the Game
- 🎯 Football Tactics
- 📈 Player Comparisons
- 🎮 EA Sports FC / FIFA Games
""")

    st.markdown("---")

    st.subheader("📚 Knowledge Base")

    st.markdown("""
✅ IFAB Laws of the Game

✅ FIFA World Cup History

✅ FIFA World Cup Regulations

✅ FIFA World Cup Anecdotes

✅ UEFA Champions League Regulations

✅ Football Intelligence & Tactics
""")

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown("""
✅ Conversation Memory

✅ Automatic Model Switching

✅ Multiple AI Models

✅ Source Citations

✅ Streamlit Chat Interface

✅ Multi-Document RAG (EARLY STAGE 🔁)

🔜 Live Football API

🔜 Match Statistics

🔜 Transfer News
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

        st.session_state.bot.clear_history()

        st.session_state.messages = []

        st.rerun()

# --------------------------------------------------
# Main Page
# --------------------------------------------------

st.title("⚽ FootballGPT")

st.caption("AI-Powered Football Assistant with Retrieval-Augmented Generation")

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

    # -------------------------
    # User Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # -------------------------
    # Assistant Message
    # -------------------------

    with st.chat_message("assistant"):

        with st.spinner("⚽ Searching football knowledge..."):

            result = st.session_state.bot.chat(prompt)

            st.success("📚 Answer generated using Football Knowledge Base")

            st.caption(
                f"🤖 {result['model']} • {result['provider']}"
            )

            st.markdown(result["answer"])

            if result.get("sources"):

                with st.expander("📖 Sources Used"):

                    for source in result["sources"]:

                        if "laws_of_the_game" in source:

                            st.write("📘 Laws of the Game — " + source.split("(")[1].replace(")", ""))

                        elif "fifa_world_cup_history" in source:

                            st.write("🌍 FIFA World Cup History — " + source.split("(")[1].replace(")", ""))

                        elif "fifa_world_cup_regulations" in source:

                            st.write("📜 FIFA World Cup Regulations — " + source.split("(")[1].replace(")", ""))

                        elif "fifa_world_cup_anecdotes" in source:

                            st.write("📖 FIFA World Cup Anecdotes — " + source.split("(")[1].replace(")", ""))

                        elif "uefa_champions_league_regulations" in source:

                            st.write("🏆 UEFA Champions League Regulations — " + source.split("(")[1].replace(")", ""))

                        elif "football_intelligence_and_tactics" in source:

                            st.write("🎯 Football Intelligence & Tactics — " + source.split("(")[1].replace(")", ""))

                        else:

                            st.write(source)

    # -------------------------
    # Save Assistant Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"]
        }
    )