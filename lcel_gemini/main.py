
# os : permet de manipuler les variables d'environnement 
# récupérer la clé API depuis le système ou le fichier .env
import os

# # On l'utilise pour extraire les sous-questions et les réponses
import re

# load_dotenv : permet de charger les variables du fichier .env
from dotenv import load_dotenv

# connecter LangChain à Gemini
from langchain_google_genai import ChatGoogleGenerativeAI

# créer des prompts dynamiques
from langchain_core.prompts import PromptTemplate

# transforme la réponse du modèle en chaîne de caractères
from langchain_core.output_parsers import StrOutputParser

# RunnableLambda	Intégration de fonctions Python dans LCEL
# RunnablePassthrough	Conservation et enrichissement des données
from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough
)


# ==========================================
# 1. CONFIGURATION GEMINI
# ==========================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") #lire variable d'environnement GOOGLE_API_KEY

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY introuvable dans le fichier .env")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

print("✅ Gemini 2.5 Flash configuré")


# ==========================================
# 2. DECOMPOSITION DE LA QUESTION
# ==========================================

decompose_prompt = PromptTemplate.from_template(
    """
    Décomposez la question suivante en maximum 3 sous-questions
    courtes, claires et complémentaires.

    Retournez uniquement une liste numérotée :
    1. ...
    2. ...
    3. ...

    Question :
    {question}
    """
)

# chaine LCEL
decompose_chain = (
    decompose_prompt
    | llm
    | StrOutputParser()
)


# Fonction de parsing avec Regex
def parse_numbered_subquestions(text):

    # Diviser le texte en plusieurs lignes
    lines = text.strip().splitlines() 

    # Liste qui contiendra les sous-questions extraites
    subquestions = []

    for line in lines:

        # Vérifier si la ligne commence par un numéro: 1. Comment fonctionne une API ?
        match = re.match(
            r"^\s*\d+\s*[.)]\s*(.+\S)\s*$",
            line
        )

        if match:
            # Récupérer uniquement le texte de la question
            subquestions.append(match.group(1).strip())

    if not subquestions:
        # on conserve le texte complet comme une seule question
        subquestions = [text.strip()]

    # Retourner au maximum 3 sous-questions
    return subquestions[:3]


parse_subq_runnable = RunnableLambda(
    parse_numbered_subquestions
)


# ==========================================
# 3. REPONDRE AUX SOUS-QUESTIONS
# ==========================================

answer_prompt = PromptTemplate.from_template(
    """
    Vous êtes un assistant pédagogique et précis.

    Répondez à la sous-question suivante.

    Respectez exactement ce format :

    Réponse : <réponse en une ligne>

    Justifications :
    - <justification 1>
    - <justification 2>

    Soyez clair et concis.

    Sous-question :
    {subq}
    """
)

answer_chain = (
    answer_prompt
    | llm
    | StrOutputParser()
)


# Exécution des réponses en parallèle

def run_answers(subquestions):

    # Transformer les sous-questions en dictionnaires
    inputs = [
        {"subq": q}
        for q in subquestions
    ]

    # Exécuter plusieurs appels à la chaîne
    outputs = answer_chain.batch(
        inputs,
        # max_concurrency=3 signifie que nous autorisons jusqu'à trois traitements simultanés.
        config={"max_concurrency": 3}
    )

    parsed = []

    for output in outputs:

        # Variable pour stocker la réponse principale
        answer_line = None

         # Liste des justifications
        steps = []

        for line in output.splitlines():

            # Chercher la ligne qui commence par Réponse :
            if re.match(r"^\s*Réponse\s*:", line, re.IGNORECASE):

                answer_line = line.split(":", 1)[1].strip()

            # Chercher les lignes qui commencent par - ou •
            elif re.match(r"^\s*[-•]\s+", line):

                step = re.sub(
                    r"^\s*[-•]\s+",
                    "",
                    line
                ).strip()

                steps.append(step)

        # Organiser les informations dans un dictionnaire
        parsed.append({
            "answer": answer_line or output,
            "steps": steps or ["Aucune justification extraite"],
            "raw": output
        })

    return parsed


# ==========================================
# 4. SYNTHESE FINALE
# ==========================================

combine_prompt = PromptTemplate.from_template(
    """
    Synthétisez les réponses suivantes en une réponse finale concise.

    Réponses et justifications :

    {subanswers_text}

    Retournez exactement trois lignes :

    1) Réponse finale : <une seule ligne>
    2) Points clés : - <point 1> ; - <point 2>
    3) Niveau de confiance : <faible / moyen / élevé>

    Ne rajoutez aucune autre ligne.
    """
)


def format_subanswers_block(data):

    blocks = []

    # enumerate() permet de parcourir une liste tout en récupérant son index.
    for i, answer in enumerate(data["answers"], start=1):

        # Ajouter la réponse principale
        blocks.append(
            f"{i}. Réponse : {answer['answer']}"
        )

        # Ajouter le titre des justifications
        blocks.append("Justifications :")

        # Ajouter chaque justification
        for step in answer["steps"]:
            blocks.append(f"- {step}")

    # Regrouper toutes les lignes dans une seule chaîne
    return {
        "subanswers_text": "\n".join(blocks)
    }


combine_chain = (
    RunnableLambda(format_subanswers_block)
    | combine_prompt
    | llm
    | StrOutputParser()
)


# ==========================================
# 5. PIPELINE LCEL COMPLET
# ==========================================

def enrich_with_answers(data):

    # Récupérer les sous-questions
    # Puis demander à Gemini d'y répondre
    answers = run_answers(data["subquestions"])

    # Conserver les données existantes
    # et ajouter les réponses obtenues
    return {
        **data,
        "answers": answers
    }


answer_runnable = RunnableLambda(
    enrich_with_answers
)


pipeline = (
    {
        "subquestions": decompose_chain | parse_subq_runnable
    }
    | answer_runnable
    | RunnablePassthrough.assign(
        final=combine_chain
    )
)


# ==========================================
# 6. EXECUTION SUR DEUX QUESTIONS
# ==========================================

questions = [

    "Comment améliorer les performances et réduire la latence d'une application web qui utilise un modèle de Machine Learning ?",

    "Comment sécuriser une API REST développée avec Python et FastAPI ?"

]


for index, question in enumerate(questions, start=1):

    print("\n" + "=" * 70)
    print(f"TEST {index}")
    print("=" * 70)

    print("\nQUESTION :")
    print(question)

    result = pipeline.invoke({
        "question": question
    })

    print("\n1. SOUS-QUESTIONS DECOMPOSEES :")

    for i, subq in enumerate(result["subquestions"], start=1):
        print(f"{i}. {subq}")

    print("\n2. SOUS-REPONSES :")

    for i, answer in enumerate(result["answers"], start=1):

        print(f"\nSous-question {i}")
        print(answer["raw"])

    print("\n3. SYNTHESE FINALE :")
    print(result["final"])

    print("\n" + "=" * 70)


# ==========================================
# 7. TEST UNITAIRE
# ==========================================

def test_max_three_subquestions():

    sample_output = """
    1. Comment fonctionne une API REST ?
    2. Quels sont ses avantages ?
    3. Comment sécuriser une API ?
    4. Comment tester une API ?
    """

    result = parse_numbered_subquestions(sample_output)

    assert len(result) <= 3

    print("\n✅ Test réussi : maximum 3 sous-questions.")


test_max_three_subquestions()
