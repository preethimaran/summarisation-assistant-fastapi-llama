from openai import OpenAI
from IPython.display import Markdown, display
from app.config import OLLAMA_API_KEY, MODEL_NAME

def text_summariser(content):

    system_prompt = """
    You are a helpful AI assistant. Your task is to generate a clear and concise summary of the text provided as input. The summary should be tailored for UK students studying coursework.

    - Do NOT use introductory phrases like “here is the summary.”
    - Focus on making the summary easy to read and understand quickly.
    - Avoid unnecessary commentary or personal opinions.
    """
    OLLAMA_BASE_URL_CHAT="http://localhost:11434/v1/"
    ollama = OpenAI(base_url=OLLAMA_BASE_URL_CHAT, api_key=OLLAMA_API_KEY)
    user_prompt = content
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    responses = ollama.chat.completions.create(model=MODEL_NAME, messages=messages)
    return responses.choices[0].message.content
    
    

