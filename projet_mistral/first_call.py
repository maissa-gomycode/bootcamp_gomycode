
import os
from dotenv import load_dotenv
from mistralai.client import Mistral

# 1. Charger les variables du fichier .env
load_dotenv()

# 2. Récupérer la clé API
api_key = os.environ["MISTRAL_API_KEY"]

# 3. Créer le client Mistral
client = Mistral(api_key=api_key)

# 4. Définir les messages
messages = [
    {
        "role": "system",
        "content": (
            "Tu es un assistant pédagogique spécialisé en informatique. "
            "Explique les concepts avec des mots simples. "
            "Utilise des phrases courtes et donne toujours un exemple pratique."
        )
    },
    {
        "role": "user",
        "content": "Explique-moi la programmation orientée objet."
    }
]

# 5. Envoyer la requête au modèle
try:
    response = client.chat.complete(
        model="mistral-small-2603",
        messages=messages
    )

    # 6. Afficher la réponse
    print("Réponse de Mistral :")
    print(response.choices[0].message.content)

except Exception as error:
    print("Une erreur s'est produite :", error)
