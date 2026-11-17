
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Configuration
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(api_version="v1beta")
)

# Historique de la conversation
SYSTEM_PROMPT = """
Tu es un professeur de Python.
Tu expliques simplement avec des exemples.
Tu réponds en français.
"""

messages = [
    {
        "role": "user",
        "parts": [{"text": SYSTEM_PROMPT}]
    }
]

# Conversation
while True:

    user_message = input("Vous : ")

    if user_message.lower() == "exit":
        print("Fin de la conversation.")
        break

    messages.append({
        "role": "user",
        "parts": [{"text": user_message}]
    })

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )

    assistant_message = response.text

    print("Assistant :", assistant_message)

    messages.append({
        "role": "model",
        "parts": [{"text": assistant_message}]
    })
