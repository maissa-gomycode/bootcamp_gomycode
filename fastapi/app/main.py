
from fastapi import FastAPI
from app.routers import chat

app = FastAPI(
    title="API Backend",
    description="Backend FastAPI connecté à Gemini.",
    version="1.0.0"
)

app.include_router(chat.router)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "L'API est en cours d'exécution"
    }
