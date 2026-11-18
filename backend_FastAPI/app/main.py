
from fastapi import FastAPI

from app.routers import health, chat, quiz, summarise


# ==========================================
# CREATION DE L'APPLICATION
# ==========================================

app = FastAPI(
    title="Learning Backend API",
    description="API pédagogique avec FastAPI",
    version="1.0.0"
)


# ==========================================
# ENREGISTREMENT DES ROUTEURS
# ==========================================

app.include_router(health.router)
app.include_router(chat.router)
app.include_router(quiz.router)
app.include_router(summarise.router)


# ==========================================
# ENDPOINT RACINE
# ==========================================

@app.get("/")
def root():

    return {
        "message": "Bienvenue sur notre API Backend",
        "documentation": "/docs"
    }
