
import os
from dotenv import load_dotenv
from mistralai.client import Mistral

# 1. Charger les variables du fichier .env
load_dotenv()

# 2. Récupérer la clé API
api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    raise ValueError("La clé API MISTRAL_API_KEY est introuvable.")

# 3. Créer le client Mistral
client = Mistral(api_key=api_key)

# 4. Initialiser l'historique de conversation
messages = [
    {
        "role": "system",
        "content": (
            "Tu es un assistant pédagogique sympathique. "
            "Tu aides les étudiants à apprendre Python. "
            "Explique les concepts simplement et donne des exemples pratiques."
        )
    }
]

print("=== Chatbot Python avec Mistral ===")
print("Pose tes questions ! (Tape 'quit' ou 'exit' pour quitter)\n")

# 5. Boucle de conversation
while True:

    user_text = input("Vous : ").strip()

    if user_text.lower() in ("quit", "exit"):
        print("Fin de la conversation.")
        break

    if not user_text:
        continue

    # Ajouter la question de l'utilisateur
    messages.append({
        "role": "user",
        "content": user_text
    })

    try:
        # Envoyer toute la conversation à Mistral
        response = client.chat.complete(
            model="mistral-small-2603",
            messages=messages,
            temperature=0.3,
            max_tokens=300
        )

        # Récupérer la réponse
        answer = response.choices[0].message.content

        print("\nAssistant :", answer, "\n")

        # Ajouter la réponse à l'historique
        messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as error:
        print("Erreur :", error)

        # Retirer la question si la requête a échoué
        messages.pop()
