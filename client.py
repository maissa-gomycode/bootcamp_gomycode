# Le client OpenAI est comme un intermédiaire entre notre application et le service d'intelligence artificielle.

from openai import OpenAI  #permet de créer le client.
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Récupérer la clé API
api_key = os.getenv("GEMINI_API_KEY")

# Vérifier la clé
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Créer le client OpenAI
client = OpenAI(api_key=api_key)

# Confirmation
print("Client OpenAI prêt")