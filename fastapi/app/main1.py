
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, timezone


# ==================================================
# 1. CONFIGURATION DE L'APPLICATION FASTAPI
# ==================================================

# FastAPI() crée notre application backend.
# title, description et version permettent de personnaliser
# la documentation automatique de l'API (Swagger).
app = FastAPI(
    title="Mon API Backend",
    description="Un premier backend FastAPI pour mon projet.",
    version="1.0.0"
)


# ==================================================
# 2. MODÈLES DE DONNÉES (PYDANTIC)
# ==================================================

# Un modèle Pydantic définit la structure des données
# que le client doit envoyer à notre API.

# Modèle pour recevoir un message destiné à l'endpoint /chat.
class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000
    )


# Modèle pour recevoir les paramètres de création d'un quiz.
class QuizRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=2,
        max_length=100
    )
    # Nombre de questions : 3 par défaut, entre 1 et 10.
    num_questions: int = Field(
        default=3,
        ge=1,
        le=10
    )


# Modèle pour recevoir le texte à résumer.
class SummariseRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=20,
        max_length=5000
    )
    # Nombre de points du résumé : 3 par défaut, entre 1 et 5.
    max_bullets: int = Field(
        default=3,
        ge=1,
        le=5
    )


# Modèle qui définit la structure d'une réponse du chatbot.
class ChatResponse(BaseModel):
    answer: str
    model: str
    tokens_used: int


# ==================================================
# 3. ENDPOINT GET /
# ==================================================

# GET permet de récupérer des informations.
# Cet endpoint affiche un message de bienvenue.
@app.get("/")
def root():
    return {
        "message": "Bienvenue sur mon API backend"
    }


# ==================================================
# 4. ENDPOINT GET /health
# ==================================================

# Cet endpoint permet de vérifier si l'API fonctionne.
@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "API is running",

        # datetime.now() récupère la date et l'heure actuelles.
        # timezone.utc indique que l'heure est en UTC.
        "timestamp": datetime.now(timezone.utc).isoformat(),

        "version": "1.0.0"
    }


# ==================================================
# 5. ENDPOINT POST /chat
# ==================================================

# POST permet d'envoyer des données à l'API.
# Le paramètre request contient les données envoyées
# par le client, validées selon le modèle ChatRequest.
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # strip() supprime les espaces au début et à la fin.
    # Cette vérification empêche d'accepter un message
    # qui contient uniquement des espaces.
    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Le message ne peut pas être vide."
        )

    # request.message permet de récupérer le message envoyé
    # par le client.
    # Pour le moment, nous utilisons une réponse fictive.
    return {
        "answer": f"You asked: {request.message}",
        "model": "placeholder",
        "tokens_used": 0
    }


# ==================================================
# 6. ENDPOINT POST /quiz
# ==================================================

# Cet endpoint génère un quiz à partir d'un sujet.
@app.post("/quiz")
def quiz(request: QuizRequest):

    # Liste vide qui va contenir les questions du quiz.
    questions = []

    # La boucle génère le nombre de questions demandé.
    for index in range(1, request.num_questions + 1):

        questions.append({
            "question": f"Question {index} about {request.topic}",

            # Quatre choix de réponses pour chaque question.
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],

            # Réponse fictive pour cet exemple.
            "answer": "Option A"
        })

    # Retourne le sujet, le nombre de questions
    # et la liste des questions au format JSON.
    return {
        "topic": request.topic,
        "num_questions": request.num_questions,
        "questions": questions
    }


# ==================================================
# 7. ENDPOINT POST /summarise
# ==================================================

# Cet endpoint reçoit un texte et retourne un résumé fictif.
@app.post("/summarise")
def summarise(request: SummariseRequest):

    # split() découpe le texte en mots.
    words = request.text.split()

    # Retourne un résumé et le nombre de mots du texte.
    # Pour le moment, le résumé est un placeholder.
    return {
        "summary": [
            "This is a placeholder summary.",
            "The real summarization logic will be connected later."
        ][:request.max_bullets],

        "word_count": len(words)
    }


# ==================================================
# 8. ENDPOINT GET /about
# ==================================================

# Cet endpoint fournit des informations sur le projet.
@app.get("/about")
def about():
    return {
        "projet": "Mon backend FastAPI",
        "objectif": "Exposer les fonctionnalités de Python via une API",
        "statut": "Apprentissage des fondamentaux du développement backend"
    }
