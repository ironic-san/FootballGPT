from dotenv import load_dotenv
import os

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# --------------------------------------------------
# Application Information
# --------------------------------------------------

APP_NAME = "FootballGPT"

VERSION = "3.0"

# --------------------------------------------------
# AI Models (Priority Order)
# --------------------------------------------------

MODELS = [

    {
        "name": "Gemini 3.1 Flash Lite",
        "id": "gemini-3.1-flash-lite",
        "provider": "Google",
        "priority": 1
    },

    {
        "name": "Gemini 2.5 Flash",
        "id": "gemini-2.5-flash",
        "provider": "Google",
        "priority": 2
    },

    {
        "name": "Gemma 4 26B",
        "id": "gemma-4-26b",
        "provider": "Google",
        "priority": 3
    }

]

# --------------------------------------------------
# Chat Settings
# --------------------------------------------------

MAX_HISTORY = 20

TEMPERATURE = 0.7

# --------------------------------------------------
# Future RAG Settings
# --------------------------------------------------

RAG_ENABLED = False

TOP_K = 5

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100