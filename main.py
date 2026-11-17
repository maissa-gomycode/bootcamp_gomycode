from google import genai
from google.genai import types
from google.genai import errors
from dotenv import load_dotenv
import os
import time

# Charger les variables d'environnement
load_dotenv()

# Récupérer la clé API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY introuvable")

# Créer le client Gemini
# client = genai.Client(api_key=api_key)
client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        api_version="v1beta"
    )
)


def call_ai(question):

    try:
        # Envoyer une requête
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question,
            config=types.GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=800,
                system_instruction=(
                    "Tu es un formateur en informatique. "
                    "Explique les concepts simplement avec des exemples."
                )
            )
        )
        return response

    except errors.APIError as e:

        if e.code == 401 or e.code == 403:
            print("Erreur d'authentification. Vérifiez votre clé API.")

        elif e.code == 429:
            print("Limite de requêtes atteinte. Réessayez plus tard.")

        else:
            print(f"Erreur API : {e.message}")

        return None

    except Exception as e:

        print(f"Une erreur inattendue est survenue : {e}")
        return None


# Tester la fonction
response = call_ai("Explique-moi les API REST.")

if response:

    # Afficher la réponse
    print("\n--- Réponse de Gemini ---")
    print(response.text)

    # Afficher les statistiques des jetons
    usage = response.usage_metadata

    if usage:
        print("\n--- Utilisation des jetons ---")

        print("Jetons en entrée :",
              usage.prompt_token_count)

        print("Jetons en sortie :",
              usage.candidates_token_count)

        print("Total des jetons :",
              usage.total_token_count)

    else:
        print("Informations sur les jetons indisponibles.")
