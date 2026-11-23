from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database import engine, Base
from app.routes import conversations
from app.routes import courses
from app.routes import auth
from app import models  # Importer les modèles
from app.dependencies import get_current_user
from app.models import User
from app.database import get_db

app = FastAPI(
    title="Study Buddy API",
    description="Backend sécurisé pour un assistant intelligent",
    version="1.0.0"
)

app.include_router(conversations.router)
app.include_router(courses.router)
app.include_router(auth.router)

# Création des tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Study Buddy API"}

# @app.get("/db-test")
# def test_database(db: Session = Depends(get_db)):
#     return {
#         "message": "Connexion à la base de données réussie !"
#     }

@app.get("/db-test")
def test_database(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "message": "Connexion à SQLite réussie !"
    }

@app.get("/users/me")
def read_current_user(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "email": current_user.email
    }