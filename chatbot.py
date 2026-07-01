from prompts import SYSTEM_PROMPT
from model_manager import ModelManager
from config import MAX_HISTORY
from rag import FootballRAG


class FootballChatbot:
    """
    FootballGPT Chatbot

    Responsibilities:
    - Manage conversation history
    - Retrieve football knowledge using RAG
    - Build the final prompt
    - Generate responses using the Model Manager
    """

    def __init__(self):

        self.manager = ModelManager()

        # Load Vector Database once
        self.rag = FootballRAG()
        self.rag.load_database()

        # Conversation history
        self.history = [SYSTEM_PROMPT]

    # --------------------------------------------------
    # Properties
    # --------------------------------------------------

    @property
    def current_model(self):
        return self.manager.current_model

    @property
    def current_provider(self):
        return self.manager.current_provider

    # --------------------------------------------------
    # Conversation
    # --------------------------------------------------

    def clear_history(self):

        self.history = [SYSTEM_PROMPT]

    def _trim_history(self):

        if len(self.history) > MAX_HISTORY:

            system_prompt = self.history[0]

            recent = self.history[-(MAX_HISTORY - 1):]

            self.history = [system_prompt] + recent

    # --------------------------------------------------
    # Build RAG Context
    # --------------------------------------------------

    def _build_context(self, query):

        docs = self.rag.retrieve(query)

        context = []

        sources = []

        for doc in docs:

            source = doc.metadata.get("source", "Unknown")

            page = doc.metadata.get("page_label", "?")

            sources.append(f"{source} (Page {page})")

            context.append(

                f"""
Source: {source}
Page: {page}

{doc.page_content}
"""

            )

        # Remove duplicate sources
        sources = list(dict.fromkeys(sources))

        return "\n\n".join(context), sources

    # --------------------------------------------------
    # Chat
    # --------------------------------------------------

    def chat(self, user_input):

        # Save user message
        self.history.append(f"User: {user_input}")

        self._trim_history()

        # Retrieve football knowledge
        context, sources = self._build_context(user_input)

        # Conversation history
        conversation = "\n".join(self.history)

        # Final Prompt
        prompt = f"""
{SYSTEM_PROMPT}

You are FootballGPT.

You have access to official football documents.

Instructions:

- Prefer the retrieved context whenever it answers the user's question.
- If the retrieved context is incomplete, use your football knowledge.
- Never invent rules that contradict the retrieved documents.
- Answer naturally.
- Use bullet points whenever useful.
- Keep explanations clear and concise.

======================================================
Retrieved Football Knowledge
======================================================

{context}

======================================================
Conversation
======================================================

{conversation}

Assistant:
"""

        result = self.manager.generate(prompt)

        answer = result["answer"]

        # Save assistant response
        self.history.append(f"Assistant: {answer}")

        # Return sources for Streamlit UI
        result["sources"] = sources

        return result