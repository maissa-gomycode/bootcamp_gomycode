
# ==================================================
# IMPORTATIONS
# ==================================================

import os

from dotenv import load_dotenv
from google import genai
from google.genai import errors


# ==================================================
# 1. CHARGEMENT DE LA CONFIGURATION
# ==================================================

# Charge les variables présentes dans le fichier .env
load_dotenv()

# Récupère la clé API Gemini
api_key = os.getenv("GEMINI_API_KEY")

# Vérifie que la clé API existe
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY introuvable dans les variables d'environnement."
    )


# ==================================================
# 2. CRÉATION DU CLIENT GEMINI
# ==================================================

# Le client permet de communiquer avec l'API Gemini
client = genai.Client(api_key=api_key)


# ==================================================
# 3. INSTRUCTIONS DU MODÈLE
# ==================================================

SYSTEM_PROMPT = """
Vous êtes un assistant d'apprentissage.

Expliquez clairement les concepts et utilisez des exemples
lorsque cela est pertinent.

Si la question n'est pas claire, demandez des précisions.
"""


# ==================================================
# 4. FONCTION D'APPEL DU MODÈLE LLM
# ==================================================

def call_llm(user_message: str) -> dict:

    try:

        # Envoie une requête au modèle Gemini
        response = client.models.generate_content(

            # Nom du modèle utilisé
            model="gemini-2.5-flash",

            # Instructions et message utilisateur
            contents=user_message,

            # Configuration du modèle
            config={
                "system_instruction": SYSTEM_PROMPT,
                "temperature": 0.3,
                "max_output_tokens": 700
            }
        )

        # Récupère le contenu de la réponse générée
        answer = response.text or ""

        # Récupère le nombre total de tokens utilisés
        tokens_used = (
            response.usage_metadata.total_token_count
            if response.usage_metadata
            else 0
        )

        # Retourne les informations sous forme de dictionnaire
        return {
            "answer": answer,
            "model": "gemini-2.5-flash",
            "tokens_used": tokens_used
        }

    # Erreur liée à une clé API invalide
    except errors.ClientError as e:

       
        print(f"Erreur Gemini : {e}")

        if e.code in (401, 403):
            raise RuntimeError("Clé API invalide ou accès refusé.")

        if e.code == 429:
            raise RuntimeError("Limite d'utilisation Gemini atteinte.")

        raise RuntimeError(f"Erreur API Gemini : {e}")

    except Exception as e:

        print(f"Erreur inattendue : {type(e).__name__}: {e}")

        raise RuntimeError(f"Erreur interne Gemini : {e}")
