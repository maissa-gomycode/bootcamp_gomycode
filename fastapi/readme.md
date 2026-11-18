# Backend API avec FastAPI et Gemini

## 1. Présentation du projet

Ce projet consiste à développer une API Backend avec **FastAPI**, connectée à un modèle d'intelligence artificielle via l'API **Google Gemini**.

L'objectif est de comprendre comment construire un backend professionnel capable de :

- Recevoir des requêtes HTTP.
- Vérifier et valider les données reçues.
- Exécuter une logique métier.
- Communiquer avec un service externe d'intelligence artificielle.
- Retourner des réponses au format JSON.
- Gérer les erreurs.
- Tester automatiquement les endpoints.

### Technologies utilisées

| Technologie | Rôle |
|---|---|
| Python | Langage de programmation backend. |
| FastAPI | Framework de création d'API. |
| Uvicorn | Serveur d'exécution de l'application FastAPI. |
| Pydantic | Validation et structuration des données. |
| Gemini API | Fournisseur du modèle d'intelligence artificielle. |
| pytest | Exécution des tests automatisés. |
| httpx | Envoi de requêtes HTTP dans les tests. |
| Swagger UI | Documentation et tests interactifs de l'API. |
| curl | Tests HTTP depuis le terminal. |
| python-dotenv | Chargement des variables d'environnement. |

---

## 2. Comprendre le fonctionnement d'une API Backend

Une API (Application Programming Interface) permet à plusieurs applications de communiquer entre elles.

Dans notre projet, le fonctionnement est le suivant :

1. **Frontend / Client :** l'utilisateur saisit un message et l'envoie.
2. **FastAPI :** reçoit la requête HTTP.
3. **Pydantic :** vérifie la structure et la validité des données.
4. **Router :** identifie l'endpoint correspondant.
5. **Service :** exécute la logique métier et communique avec Gemini.
6. **Gemini API :** génère une réponse.
7. **FastAPI :** retourne une réponse JSON au client.

### Architecture générale

Frontend / Client
↓
Requête HTTP
↓
FastAPI
↓
Validation Pydantic
↓
Router
↓
Service Python
↓
Gemini API
↓
Réponse JSON

### Notions fondamentales

**API :** interface permettant à deux applications de communiquer.

**Endpoint :** point d'accès spécifique à une fonctionnalité de l'API.

Exemples :
- GET /health
- POST /chat

**HTTP :** protocole utilisé pour échanger des données entre un client et un serveur.

**JSON :** format léger utilisé pour transmettre des données.

Exemple :

```json
{
    "message": "Bonjour, explique-moi FastAPI."
}
```

**Backend :** partie d'une application qui traite les données, applique les règles métier et communique avec les services externes.

**Frontend :** partie visible de l'application avec laquelle l'utilisateur interagit.

---

## 3. Comprendre les méthodes HTTP

Les méthodes HTTP indiquent l'action que le client souhaite effectuer.

| Méthode | Utilisation | Exemple |
|---|---|---|
| GET | Récupérer des informations. | GET /health |
| POST | Envoyer des données ou créer une ressource. | POST /chat |
| PUT | Remplacer une ressource. | PUT /users/1 |
| PATCH | Modifier partiellement une ressource. | PATCH /users/1 |
| DELETE | Supprimer une ressource. | DELETE /users/1 |

Dans notre projet :

- GET /health permet de vérifier que le backend fonctionne.
- POST /chat permet d'envoyer un message au modèle Gemini.

### Codes de statut HTTP

Les codes HTTP indiquent le résultat d'une requête.

| Code | Signification | Exemple |
|---|---|---|
| 200 | OK | Requête exécutée avec succès. |
| 201 | Created | Ressource créée. |
| 400 | Bad Request | Message vide selon notre règle métier. |
| 401 | Unauthorized | Authentification manquante ou invalide. |
| 403 | Forbidden | Accès interdit. |
| 404 | Not Found | Endpoint inexistant. |
| 422 | Unprocessable Entity | Données invalides selon Pydantic. |
| 429 | Too Many Requests | Limite de requêtes atteinte. |
| 500 | Internal Server Error | Erreur interne du serveur. |
| 503 | Service Unavailable | Service temporairement indisponible. |

**Bonne pratique :** choisir un code HTTP cohérent avec le résultat de l'opération.

---

## 4. Installation et configuration du projet

### 4.1. Créer un environnement virtuel

Un environnement virtuel permet d'isoler les dépendances d'un projet Python.

Sous Windows :

```bash
python -m venv venv
```

Activer l'environnement sous Git Bash :

```bash
source venv/Scripts/activate
```

Sous Windows CMD :

```bash
venv\Scripts\activate
```

### 4.2. Installer les dépendances

```bash
pip install fastapi uvicorn google-genai python-dotenv pytest httpx pytest-asyncio
```

### 4.3. Structure du projet

```text
openai_secure_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── chat.py
│   │
│   └── services/
│       ├── __init__.py
│       └── ai.py
│
├── tests/
│   ├── test_health.py
│   └── test_chat_validation.py
│
├── docs/
│   └── api-test-results.md
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### 4.4. Rôle des fichiers

| Fichier / Dossier | Responsabilité |
|---|---|
| app/ | Contient le code backend. |
| main.py | Initialise l'application FastAPI et enregistre les routeurs. |
| routers/ | Contient les endpoints et gère les requêtes HTTP. |
| services/ | Contient la logique métier et les appels aux services externes. |
| tests/ | Contient les tests automatisés. |
| docs/ | Contient la documentation du projet et les résultats des tests. |
| .env | Stocke les variables d'environnement. |
| .gitignore | Indique les fichiers à exclure de Git. |
| requirements.txt | Liste les dépendances Python. |
| README.md | Présente le projet et explique son utilisation. |

**Bonne pratique :** séparer les responsabilités permet de rendre le code plus lisible, maintenable et évolutif.

---

## 5. Comprendre le rôle de Pydantic

Pydantic permet de définir la structure des données attendues par une API et de vérifier leur validité.

Exemple dans `routers/chat.py` :

```python
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):

    message: str = Field(
        ...,
        min_length=1,
        max_length=2000
    )
```

### Explication

- `BaseModel` : définit un modèle de données.
- `message: str` : indique que le message doit être une chaîne de caractères.
- `Field(...)` : permet de définir des contraintes.
- `...` : indique que le champ est obligatoire.
- `min_length=1` : impose une longueur minimale.
- `max_length=2000` : limite la longueur du message.

Autres paramètres utiles :

| Paramètre | Signification |
|---|---|
| gt | Strictement supérieur à. |
| ge | Supérieur ou égal à. |
| lt | Strictement inférieur à. |
| le | Inférieur ou égal à. |
| default | Définit une valeur par défaut. |

### Exemple avec plusieurs champs

```python
class QuizRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    num_questions: int = Field(
        default=5,
        ge=1,
        le=10
    )
```

Ici :
- Le sujet est obligatoire.
- Le nombre de questions est facultatif.
- Sa valeur par défaut est 5.
- Il doit être compris entre 1 et 10.

**À retenir :** Pydantic vérifie les données avant leur traitement par la logique métier.

---

## 6. Comprendre les modèles de réponse

Un modèle de réponse définit la structure des données retournées par l'API.

Exemple :

```python
class ChatResponse(BaseModel):

    answer: str
    model: str
    tokens_used: int
```

Une réponse JSON peut être :

```json
{
    "answer": "FastAPI est un framework Python...",
    "model": "gemini-2.5-flash",
    "tokens_used": 125
}
```

### Différence entre les modèles

| Modèle | Rôle |
|---|---|
| ChatRequest | Définit les données reçues par l'API. |
| ChatResponse | Définit les données retournées par l'API. |

**Bonne pratique :** utiliser des modèles de requête et de réponse pour garantir une structure cohérente des échanges.

---

## 7. Comprendre HTTPException et la gestion des erreurs

`HTTPException` permet de retourner une erreur HTTP avec un code de statut et un message explicatif.

Exemple :

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=400,
    detail="Le message ne peut pas être vide."
)
```

Résultat :

```json
{
    "detail": "Le message ne peut pas être vide."
}
```

### Différentes catégories d'erreurs

- Erreurs de validation : données incorrectes ou champs manquants.
- Erreurs métier : règle de l'application non respectée.
- Erreurs serveur : problème pendant l'exécution.
- Erreurs de fournisseur externe : Gemini indisponible ou clé API invalide.

**Bonne pratique :** retourner des messages compréhensibles au client sans exposer les détails internes du serveur, les clés API ou les traces techniques.

---

## 8. Comprendre le rôle des routeurs et des services

Pour éviter de placer tout le code dans un seul fichier, nous séparons notre application en plusieurs couches.

### main.py

Responsabilités :
- Créer l'application FastAPI.
- Configurer les paramètres généraux.
- Enregistrer les routeurs.

### routers/chat.py

Responsabilités :
- Définir les endpoints.
- Recevoir les requêtes.
- Vérifier les données.
- Appeler les services.
- Retourner les réponses HTTP.

### services/ai.py

Responsabilités :
- Communiquer avec Gemini.
- Construire les requêtes vers le modèle.
- Récupérer les réponses.
- Gérer les erreurs liées au fournisseur.

### Principe architectural

```text
main.py
   |
   v
routers/chat.py
   |
   v
services/ai.py
   |
   v
Gemini API
```

**Bonne pratique :** un routeur ne doit pas contenir toute la logique d'appel à l'intelligence artificielle. Il délègue cette responsabilité au service.

---

## 9. Comprendre l'intégration de Gemini

Gemini est le fournisseur de notre modèle d'intelligence artificielle.

Dans ce projet, nous utilisons le SDK officiel `google-genai`.

Installation :

```bash
pip install google-genai
```

Exemple d'appel :

```python
from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explique-moi FastAPI."
)

print(response.text)
```

Dans notre architecture, cet appel est placé dans `services/ai.py`.

### Variables d'environnement

Créer un fichier `.env` :

```env
GEMINI_API_KEY=votre_cle_api
```

Charger la clé dans Python :

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
```

**Bonnes pratiques de sécurité :**

- Ne jamais écrire une clé API directement dans le code.
- Ne jamais publier le fichier `.env` sur GitHub.
- Ne jamais envoyer une clé API dans une réponse JSON.
- Vérifier que la clé existe avant de créer le client.
- Utiliser des variables d'environnement pour les informations sensibles.

Dans `.gitignore`, ajouter :

```text
.env
venv/
__pycache__/
.pytest_cache/
*.pyc
```

---

## 10. Comprendre le principe Stateless

Une API stateless (sans état) ne conserve pas automatiquement le contexte des requêtes précédentes.

Exemple :

1. L'utilisateur envoie : « Bonjour ».
2. Le backend retourne une réponse.
3. L'utilisateur envoie : « Et toi ? ».
4. Le backend traite cette nouvelle requête sans connaître automatiquement le premier message.

Pour conserver une conversation, il faut gérer explicitement l'historique.

Cela peut être réalisé avec :
- Une base de données.
- Un système de stockage de sessions.
- Un historique transmis avec la requête.
- Un mécanisme de gestion de conversations.

**À retenir :** une API stateless ne signifie pas qu'une application ne peut jamais mémoriser des informations. Cela signifie que chaque requête doit apporter ou retrouver explicitement le contexte nécessaire à son traitement.

---

## 11. Lancer et tester l'application

### 11.1. Démarrer le serveur

Depuis le dossier racine du projet :

```bash
uvicorn app.main:app --reload
```

Explication :

- `app.main` : fichier main.py situé dans le dossier app.
- `app` : objet FastAPI défini dans main.py.
- `--reload` : redémarre le serveur lorsque le code change.

### 11.2. Accéder aux interfaces

Application :

http://127.0.0.1:8000

Documentation Swagger :

http://127.0.0.1:8000/docs

Documentation alternative :

http://127.0.0.1:8000/redoc

### 11.3. Tester les endpoints disponibles

| Endpoint | Méthode | Objectif |
|---|---|---|
| /health | GET | Vérifier le fonctionnement du backend. |
| /chat | POST | Envoyer un message à Gemini. |

### GET /health

Réponse attendue :

```json
{
    "status": "ok",
    "message": "L'API est en cours d'exécution"
}
```

### POST /chat

Données à envoyer :

```json
{
    "message": "Explique-moi FastAPI simplement."
}
```

Réponse attendue :

```json
{
    "answer": "FastAPI est un framework Python...",
    "model": "gemini-2.5-flash",
    "tokens_used": 120
}
```

Les valeurs de réponse sont illustratives.

---

## 12. Tester l'API avec curl

`curl` permet d'envoyer des requêtes HTTP directement depuis le terminal.

### Tester GET /health

```bash
curl http://127.0.0.1:8000/health
```

### Tester POST /chat

Sous Git Bash :

```bash
curl -X POST http://127.0.0.1:8000/chat \
-H "Content-Type: application/json" \
-d '{"message":"Explique les API REST simplement."}'
```

Sous Windows CMD :

```bash
curl -X POST http://127.0.0.1:8000/chat ^
-H "Content-Type: application/json" ^
-d "{\"message\":\"Explique les API REST simplement.\"}"
```

---

## 13. Comprendre les tests automatisés

Les tests permettent de vérifier que le backend fonctionne conformément aux attentes.

Nous utilisons quatre outils :

| Outil | Rôle |
|---|---|
| Swagger UI | Tests manuels depuis le navigateur. |
| curl | Tests manuels depuis le terminal. |
| pytest | Exécution des tests automatisés. |
| httpx | Envoi des requêtes HTTP dans les tests. |

### Installation

```bash
pip install pytest httpx pytest-asyncio
```

### Exemple de test

Fichier `tests/test_health.py` :

```python
import pytest

from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_health_endpoint_returns_ok():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
```

### Exécuter les tests

Depuis le dossier racine :

```bash
python -m pytest -v
```

Explication :

- `pytest` : lance les tests.
- `-v` : affiche le détail de chaque test.
- `assert` : vérifie que le résultat correspond au comportement attendu.
- `ASGITransport` : permet de tester directement l'application FastAPI sans démarrer un serveur externe.

**Bonne pratique :** tester les cas réussis, les données manquantes, les valeurs incorrectes et les limites de validation.

Il est également préférable de simuler les appels à Gemini dans les tests qui vérifient la logique du service, afin d'éviter les coûts et les dépendances à un service externe.

---

## 14. Bonnes pratiques de développement Backend

### Organisation du code

- Séparer les routeurs, les services et les modèles.
- Éviter de placer toute la logique dans `main.py`.
- Utiliser des noms de fichiers et de fonctions explicites.
- Éviter la duplication du code.

### Validation des données

- Utiliser Pydantic pour les requêtes.
- Définir des longueurs minimales et maximales.
- Vérifier les champs obligatoires.
- Définir des valeurs par défaut lorsque cela est pertinent.

### Sécurité

- Protéger les clés API.
- Utiliser un fichier `.env`.
- Ajouter `.env` dans `.gitignore`.
- Ne pas exposer les erreurs internes au client.
- Ne pas publier les informations sensibles dans les logs.

### Gestion des erreurs

- Utiliser des codes HTTP cohérents.
- Gérer les erreurs des services externes.
- Éviter les exceptions silencieuses.
- Fournir des messages d'erreur compréhensibles.

### Tests

- Tester chaque endpoint important.
- Vérifier les codes de statut HTTP.
- Tester les données incorrectes.
- Automatiser les tests répétitifs.
- Documenter les résultats.

### Maintenabilité

- Utiliser un environnement virtuel.
- Centraliser les dépendances dans requirements.txt.
- Documenter le fonctionnement du projet.
- Utiliser Git pour suivre les modifications.
- Garder une architecture claire et évolutive.

---

## 15. Commandes essentielles à retenir

| Commande | Utilité |
|---|---|
| `python -m venv venv` | Créer un environnement virtuel. |
| `source venv/Scripts/activate` | Activer l'environnement sous Git Bash. |
| `pip install -r requirements.txt` | Installer les dépendances. |
| `uvicorn app.main:app --reload` | Démarrer le serveur. |
| `python -m pytest -v` | Exécuter les tests. |
| `pip freeze > requirements.txt` | Enregistrer les dépendances installées. |
| `deactivate` | Quitter l'environnement virtuel. |

---

## 16. Conclusion

Dans ce projet, nous avons découvert les fondamentaux du développement Backend avec FastAPI.

Nous avons appris à :

- Créer une API avec FastAPI.
- Comprendre les endpoints et les méthodes HTTP.
- Valider les données avec Pydantic.
- Organiser le code avec des routeurs et des services.
- Connecter le backend à Gemini.
- Gérer les erreurs et les réponses JSON.
- Tester l'API avec Swagger UI, curl, pytest et httpx.
- Appliquer les bonnes pratiques de sécurité et de maintenabilité.

**Point clé :**

Un backend professionnel ne se limite pas à recevoir des requêtes et retourner des réponses. Il doit être bien organisé, sécurisé, validé, testé et suffisamment maintenable pour évoluer avec les besoins de l'application.