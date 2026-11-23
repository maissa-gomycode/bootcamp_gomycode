
import os
import argparse

from dotenv import load_dotenv
from mistralai.client import Mistral
from openai import OpenAI


# 1. Charger les variables du fichier .env
load_dotenv()

API_KEY = os.getenv("MISTRAL_API_KEY")
MODEL = "mistral-small-latest"

# 2. Personnalité de l'assistant
SYSTEM_PROMPT = """
Tu es Study Buddy, un assistant d'étude bienveillant et patient.

Ton rôle :
- Aider les étudiants à comprendre leurs cours.
- Expliquer les notions simplement, étape par étape.
- Donner des exemples pratiques.
- Poser des questions pour vérifier la compréhension.
- Encourager l'étudiant sans le juger.
- Adapter tes explications au niveau de l'étudiant.

Réponds toujours de manière claire, pédagogique et structurée.
Si une question est difficile, divise l'explication en petites étapes.
"""

# 3. Initialiser la conversation avec le message système
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def create_client(use_openai=False):
    """Créer le client selon le fournisseur choisi."""

    if not API_KEY:
        raise ValueError(
            "La clé MISTRAL_API_KEY est absente du fichier .env."
        )

    if use_openai:
        return OpenAI(
            api_key=API_KEY,
            base_url="https://api.mistral.ai/openai/v1"
        )

    return Mistral(api_key=API_KEY)


def get_answer(client, use_openai=False):
    """Envoyer l'historique à Mistral et récupérer la réponse."""

    if use_openai:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content

    response = client.chat.complete(
        model=MODEL,
        messages=messages,
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message.content


def main():
    # 4. Lire les options de lancement
    parser = argparse.ArgumentParser(
        description="Study Buddy - Assistant d'étude avec Mistral"
    )
    parser.add_argument(
        "--openai",
        action="store_true",
        help="Utiliser le client OpenAI compatible avec Mistral"
    )
    args = parser.parse_args()

    # 5. Initialiser le client
    try:
        client = create_client(use_openai=args.openai)
    except Exception as error:
        print(f"Erreur d'initialisation : {error}")
        return

    mode = "compatible OpenAI" if args.openai else "natif Mistral"

    print("\n====================================")
    print("       Bienvenue dans Study Buddy")
    print("====================================")
    print(f"Modèle : {MODEL}")
    print(f"Mode : {mode}")
    print("Pose tes questions pour commencer.")
    print("Tape 'quit' ou 'exit' pour terminer.\n")

    # 6. Boucle de conversation
    while True:
        user_input = input("Étudiant : ").strip()

        if user_input.lower() in ["quit", "exit"]:
            print("\nStudy Buddy : Bon courage pour tes études ! À bientôt.")
            break

        if not user_input:
            continue

        # Ajouter la question à l'historique
        messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            answer = get_answer(client, use_openai=args.openai)

            # Ajouter la réponse à l'historique
            messages.append({
                "role": "assistant",
                "content": answer
            })

            print(f"\nStudy Buddy : {answer}\n")

        except Exception as error:
            # Retirer la question si l'appel a échoué
            messages.pop()

            error_message = str(error)
            print("\nStudy Buddy : Désolé, je n'ai pas pu "
                  "obtenir une réponse.")

            if "429" in error_message:
                print("La limite d'utilisation de l'API a été atteinte. "
                      "Vérifie ton quota ou réessaie plus tard.")
            elif "401" in error_message:
                print("La clé API semble invalide. Vérifie ton fichier .env.")
            else:
                print("Vérifie ta connexion Internet et la configuration "
                      "de ton API.")
                print(f"Détail technique : {error}\n")


if __name__ == "__main__":
    main()
