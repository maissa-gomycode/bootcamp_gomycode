
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# 1. Charger les variables d'environnement
load_dotenv()

# 2. Récupérer la clé API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

# 3. Initialiser le client Gemini
# client = genai.Client(api_key=api_key)

# utilises actuellement l'API v1, alors que la fonctionnalité system_instruction nécessite ici l'API v1beta.
client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        api_version="v1beta"
    )
)

# 4. Définir le prompt système
SYSTEM_PROMPT = """
Tu es un assistant pédagogique.
Tu expliques les concepts informatiques
simplement avec des exemples pratiques.
Tu réponds en français.
"""

# 5. Récupérer le message de l'utilisateur
user_message = input("Vous : ")

# 6. Envoyer la requête à Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_message,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.7
    )
)

# 7. Extraire et afficher la réponse
answer = response.text

print("\nRéponse de l'IA :")
print(answer)

# 8. Afficher les informations
print("\nModèle utilisé :", response.model_version)

usage = response.usage_metadata

print("Tokens entrée :", usage.prompt_token_count)
print("Tokens sortie :", usage.candidates_token_count)
print("Total tokens :", usage.total_token_count)
