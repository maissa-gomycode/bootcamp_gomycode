
from google import genai
from google.genai import types, errors
from dotenv import load_dotenv
import os

# ==================================
# 1. Charger les variables d'environnement
# ==================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "Clé API manquante ! "
        "Veuillez ajouter GEMINI_API_KEY dans le fichier .env"
    )


# ==================================
# 2. Créer le client Gemini
# ==================================

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        api_version="v1beta"
    )
)


# ==================================
# 3. Définir les instructions système
# ==================================

SYSTEM_INSTRUCTION = """
Tu es un assistant pédagogique spécialisé en informatique.

Tes règles :
- Réponds toujours en français.
- Explique les concepts simplement.
- Utilise des exemples pratiques.
- Adapte tes explications aux débutants.
- N'invente jamais de faits.
- Si tu ne connais pas une information, indique clairement que tu n'es pas sûr.
"""


# ==================================
# 4. Créer une conversation
# ==================================

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=0.3,
        max_output_tokens=800
    )
)


# ==================================
# 5. Fonction pour communiquer avec Gemini
# ==================================

def call_ai(question):

    try:

        response = chat.send_message(question)

        return response

    except errors.APIError as e:

        if e.code == 401 or e.code == 403:
            print("Erreur : vérifiez votre clé API et vos autorisations.")

        elif e.code == 429:
            print("Limite de requêtes atteinte. Réessayez plus tard.")

        else:
            print(f"Erreur API : {e.message}")

        return None

    except Exception as e:

        print(f"Erreur inattendue : {e}")
        return None


# ==================================
# 6. Boucle principale
# ==================================

def main():

    print("=" * 50)
    print("       BIENVENUE DANS GEMINI ASSISTANT")
    print("=" * 50)

    print("Posez vos questions en informatique.")
    print("Tapez 'help' pour afficher les commandes.")
    print("Tapez 'quit' pour quitter.")

    while True:

        question = input("\nVous : ").strip()

        if not question:
            continue

        # Commande pour quitter
        if question.lower() in ["quit", "exit"]:

            print("\nGemini : Au revoir !")
            break

        # Commande d'aide
        elif question.lower() == "help":

            print("""
Commandes disponibles :

help  : afficher les commandes
clear : réinitialiser la conversation
quit  : quitter l'application
exit  : quitter l'application
""")
            continue

        # Réinitialiser l'historique
        elif question.lower() == "clear":

            global chat

            chat = client.chats.create(
                model="gemini-2.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    temperature=0.3,
                    max_output_tokens=800
                )
            )

            print("\nGemini : Conversation réinitialisée.")
            continue

        # Envoyer la question à Gemini
        response = call_ai(question)

        if response:

            print("\nGemini :")
            print(response.text or "Aucune réponse textuelle disponible.")

            # Afficher le modèle
            print("\n--- Informations ---")
            print("Modèle utilisé : gemini-2.5-flash")

            # Afficher les jetons
            usage = response.usage_metadata

            if usage:

                print("Jetons en entrée :",
                      usage.prompt_token_count)

                print("Jetons en sortie :",
                      usage.candidates_token_count)

                print("Total des jetons :",
                      usage.total_token_count)

            else:
                print("Informations sur les jetons indisponibles.")


# ==================================
# 7. Lancer le programme
# ==================================

if __name__ == "__main__":
    main()
