
# ============================================================
# CHECKPOINT : ZERO-SHOT ET FEW-SHOT PROMPTING
# Classification automatique des e-mails avec Gemini 2.5 Flash
#
# Objectif :
# 1. Zero-Shot : classifier sans donner d'exemples.
# 2. Few-Shot : classifier avec des exemples.
#
# Technologies :
# - Python
# - Google Gen AI SDK
# - Gemini 2.5 Flash
# ============================================================


# ============================================================
# 1. IMPORTATION DES BIBLIOTHEQUES
# ============================================================

# os : permet de récupérer les variables d'environnement
import os

# load_dotenv : permet de charger les informations du fichier .env
from dotenv import load_dotenv

# genai : SDK officiel Google pour communiquer avec Gemini
from google import genai


# ============================================================
# 2. CONFIGURATION DE GEMINI
# ============================================================

# Charger les variables du fichier .env
load_dotenv()

# Récupérer la clé API Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Vérifier que la clé API existe
if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY introuvable. Vérifiez votre fichier .env"
    )

# Créer le client Gemini
client = genai.Client(
    api_key=GOOGLE_API_KEY
)

# Définir le modèle à utiliser
MODEL = "gemini-2.5-flash"

print("Gemini 2.5 Flash configuré avec succès !")


# ============================================================
# 3. FONCTION POUR INTERROGER GEMINI
# ============================================================

def ask_gemini(prompt):

    """
    Cette fonction envoie un prompt à Gemini
    et retourne sa réponse sous forme de texte.

    Paramètre :
        prompt : le texte envoyé à Gemini

    Retour :
        La réponse générée par Gemini
    """

    # Envoyer la requête au modèle Gemini
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    # Récupérer le texte généré
    return response.text.strip()


# ============================================================
# 4. ZERO-SHOT PROMPTING
# ============================================================

print("\n" + "=" * 60)
print("PARTIE 1 : ZERO-SHOT PROMPTING")
print("=" * 60)


# E-mail à classifier
email_zero_shot = """
N'oubliez pas la réunion d'équipe à 14h.
Veuillez apporter vos mises à jour de projet.
"""


# Construction du prompt Zero-Shot
# IMPORTANT : aucun exemple de classification n'est fourni.

zero_shot_prompt = f"""
Tu es un assistant spécialisé dans la classification des e-mails.

Ta tâche est de classifier l'e-mail suivant dans une seule
des trois catégories :

- Travail
- Personnel
- Spam

Règles :
- Travail : réunions, projets, tâches professionnelles,
  rapports et communications d'entreprise.
- Personnel : famille, amis, invitations et activités privées.
- Spam : messages frauduleux, publicités trompeuses,
  gains fictifs et liens suspects.

Retourne uniquement le nom de la catégorie.
N'ajoute aucune explication.

E-mail :
{email_zero_shot}
"""


# Envoyer le prompt à Gemini
zero_shot_result = ask_gemini(zero_shot_prompt)


# Afficher le résultat
print("\nE-mail :")
print(email_zero_shot)

print("Classification Zero-Shot :")
print(zero_shot_result)


# ============================================================
# 5. FEW-SHOT PROMPTING
# ============================================================

print("\n" + "=" * 60)
print("PARTIE 2 : FEW-SHOT PROMPTING")
print("=" * 60)


# Liste des e-mails à classifier
emails = [

    "Dîner à 20h ce soir ? J'apporte le vin.",

    "Vous avez gagné un iPhone gratuit ! Cliquez ici pour réclamer votre prix.",

    "Le rapport financier du deuxième trimestre est attendu demain soir.",

    "Êtes-vous libre pour déjeuner ce week-end ?"

]


# Construction du prompt Few-Shot
# Ici, nous fournissons des exemples de classification
# pour aider Gemini à comprendre la logique attendue.

few_shot_prompt = """
Tu es un assistant spécialisé dans la classification des e-mails.

Ta tâche est de classifier chaque e-mail dans une seule
des catégories suivantes :

- Travail
- Personnel
- Spam

Voici des exemples de classification :

E-mail : N'oubliez pas la réunion de l'équipe demain à 10h.
Catégorie : Travail

E-mail : Joyeux anniversaire ! J'espère te voir bientôt.
Catégorie : Personnel

E-mail : Félicitations ! Vous avez gagné 1 million d'euros.
Cliquez immédiatement pour réclamer votre cadeau.
Catégorie : Spam

E-mail : Le directeur demande le rapport financier avant vendredi.
Catégorie : Travail

E-mail : Tu es disponible pour un dîner samedi soir ?
Catégorie : Personnel


Maintenant, applique la même logique aux e-mails suivants.

Règles :
- Retourne une seule catégorie par e-mail.
- Utilise uniquement Travail, Personnel ou Spam.
- Respecte exactement le format demandé.
- Ne donne aucune explication supplémentaire.

"""


# ============================================================
# 6. CLASSIFICATION DES E-MAILS
# ============================================================

# Parcourir tous les e-mails
for index, email in enumerate(emails, start=1):

    # Ajouter l'e-mail au prompt Few-Shot
    prompt = few_shot_prompt + f"""

    E-mail :
    {email}

    Catégorie :
    """

    # Envoyer le prompt à Gemini
    result = ask_gemini(prompt)

    # Afficher le résultat
    print(f"\nE-mail {index} :")
    print(email)

    print("Catégorie :", result)


# ============================================================
# 7. FIN DU CHECKPOINT
# ============================================================

print("\n" + "=" * 60)
print("CHECKPOINT TERMINE")
print("=" * 60)
