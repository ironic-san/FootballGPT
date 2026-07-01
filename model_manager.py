from google import genai

from config import API_KEY, MODELS


class ModelManager:
    """
    Handles AI model selection and automatic failover.

    Responsibilities:
    - Initialize Gemini client
    - Try models in priority order
    - Remember last working model
    - Automatically switch on failure
    """

    def __init__(self):

        self.client = genai.Client(api_key=API_KEY)

        self.models = MODELS

        # Start with first model
        self.current_index = 0

    @property
    def current_model(self):
        """Return the currently active model name."""
        return self.models[self.current_index]["name"]

    @property
    def current_provider(self):
        """Return the provider of the current model."""
        return self.models[self.current_index]["provider"]

    def generate(self, prompt):
        """
        Generate a response using the available models.

        Returns:
        {
            "success": True/False,
            "answer": "...",
            "model": "...",
            "provider": "...",
            "error": None
        }
        """

        total_models = len(self.models)

        last_error = None

        # Start from the last successful model
        for i in range(total_models):

            index = (self.current_index + i) % total_models

            model = self.models[index]

            try:

                response = self.client.models.generate_content(
                    model=model["id"],
                    contents=prompt
                )

                # Remember this model for next request
                self.current_index = index

                return {
                    "success": True,
                    "answer": response.text,
                    "model": model["name"],
                    "provider": model["provider"],
                    "error": None
                }

            except Exception as e:

                print(f"[ModelManager] {model['name']} failed.")

                last_error = str(e)

                continue

        # No model worked
        return {
            "success": False,
            "answer": (
                "⚠️ FootballGPT couldn't generate a response.\n\n"
                "All configured AI models are currently unavailable."
            ),
            "model": None,
            "provider": None,
            "error": last_error
        }