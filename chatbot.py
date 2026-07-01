from prompts import SYSTEM_PROMPT
from model_manager import ModelManager
from config import MAX_HISTORY


class FootballChatbot:
    """
    Handles conversation memory and communicates with the Model Manager.
    """

    def __init__(self):

        self.manager = ModelManager()

        # Conversation starts with system prompt
        self.history = [SYSTEM_PROMPT]

    @property
    def current_model(self):
        return self.manager.current_model

    @property
    def current_provider(self):
        return self.manager.current_provider

    def clear_history(self):
        """Start a new conversation."""
        self.history = [SYSTEM_PROMPT]

    def _trim_history(self):
        """
        Keep only the latest conversation messages.

        The system prompt is always preserved.
        """

        if len(self.history) > MAX_HISTORY:

            system_prompt = self.history[0]

            recent_messages = self.history[-(MAX_HISTORY - 1):]

            self.history = [system_prompt] + recent_messages

    def chat(self, user_input):

        # Save user message
        self.history.append(f"User: {user_input}")

        # Prevent history from growing forever
        self._trim_history()

        # Combine into one prompt
        prompt = "\n".join(self.history)

        # Ask the Model Manager
        result = self.manager.generate(prompt)

        answer = result["answer"]

        # Save assistant reply
        self.history.append(f"Assistant: {answer}")

        return result