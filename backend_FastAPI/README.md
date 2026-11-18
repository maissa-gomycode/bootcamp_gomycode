
# Learning Backend API

## Présentation

Backend développé avec FastAPI exposant quatre endpoints :

- GET /health : vérification du backend.
- POST /chat : traitement d'un message.
- POST /quiz : génération de questions.
- POST /summarise : résumé d'un texte.

## Technologies

- Python
- FastAPI
- Uvicorn
- Pydantic
- pytest
- httpx

## Installation

Créer un environnement virtuel :

python -m venv venv

Activer l'environnement :

source venv/Scripts/activate

Installer les dépendances :

pip install -r requirements.txt

## Démarrage

uvicorn app.main:app --reload

## Documentation API

Swagger UI :

http://127.0.0.1:8000/docs

ReDoc :

http://127.0.0.1:8000/redoc

## Tests

Exécuter les tests :

python -m pytest -v

## Documentation des tests

Les résultats des tests sont disponibles dans :

docs/api-test-report.md
