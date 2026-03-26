from dotenv import load_dotenv
import os

load_dotenv(override=True)

OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")