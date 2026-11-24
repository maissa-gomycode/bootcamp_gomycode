
# ==================================================
# IMPORTATIONS
# ==================================================

import os
import asyncio

from dotenv import load_dotenv
from google import genai
from google.genai import errors


# ==================================================
# 1. CHARGEMENT DE LA CONFIGURATION
# ==================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY introuvable dans les variables d'environnement."
    )


# ==================================================
# 2. CRÉATION DU CLIENT GEMINI
# ==================================================

client = genai.Client(api_key=api_key)

MODEL = "gemini-2.5-flash"
TIMEOUT = 20


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
# 4. FONCTION ASYNCHRONE D'APPEL DU MODÈLE
# ==================================================

async def call_llm(user_message: str) -> dict:

    try:

        # Appel asynchrone à Gemini
        response = await client.aio.models.generate_content(

            model=MODEL,

            contents=user_message,

            config={
                "system_instruction": SYSTEM_PROMPT,
                "temperature": 0.3,
                "max_output_tokens": 700
            }
        )

        answer = response.text or ""

        tokens_used = (
            response.usage_metadata.total_token_count
            if response.usage_metadata
            else 0
        )

        return {
            "answer": answer,
            "model": MODEL,
            "tokens_used": tokens_used
        }

    except errors.ClientError as e:

        print(f"Erreur Gemini : {e}")

        if e.code in (401, 403):
            raise RuntimeError(
                "Clé API invalide ou accès refusé."
            )

        if e.code == 429:
            raise RuntimeError(
                "Limite d'utilisation Gemini atteinte."
            )

        raise RuntimeError("Erreur API Gemini.")

    except Exception as e:

        print(f"Erreur inattendue : {type(e).__name__}: {e}")

        raise RuntimeError(
            "Une erreur interne est survenue avec Gemini."
        )


# ==================================================
# 5. FONCTION AVEC TIMEOUT
# ==================================================

async def generate_ai_response(user_message: str) -> dict:

    try:

        result = await asyncio.wait_for(
            call_llm(user_message),
            timeout=TIMEOUT
        )

        return result

    except asyncio.TimeoutError:

        raise TimeoutError(
            "Le service Gemini met trop de temps à répondre."
        )

    except RuntimeError:
        raise

    except Exception as e:

        print(f"Erreur service IA : {e}")

        raise RuntimeError(
            "Impossible de générer une réponse IA."
        )


# ==================================================
# 6. GÉNÉRATION DU RÉSUMÉ
# ==================================================

async def generate_summary(content: str) -> str:

    prompt = f"""
    Génère un résumé clair et structuré du cours suivant.

    Cours :
    {content}
    """

    result = await generate_ai_response(prompt)

    return result["answer"]


# ==================================================
# 7. GÉNÉRATION DU QUIZ
# ==================================================

async def generate_quiz(content: str) -> str:

    prompt = f"""
    Génère un quiz de 5 questions à choix multiples
    basé sur le cours suivant.

    Indique les bonnes réponses à la fin.

    Cours :
    {content}
    """

    result = await generate_ai_response(prompt)

    return result["answer"]


# ==================================================
# 8. GÉNÉRATION DES FICHES DE RÉVISION
# ==================================================

async def generate_flashcards(content: str) -> str:

    prompt = f"""
    Génère 5 fiches de révision sous forme de questions
    et réponses basées sur le cours suivant.

    Cours :
    {content}
    """

    result = await generate_ai_response(prompt)

    return result["answer"]
