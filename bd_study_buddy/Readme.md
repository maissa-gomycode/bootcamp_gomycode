## Structure du projet

```text
bd_study_buddy/
├── app/
│   ├── cache/
│   │   └── redis_cache.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── conversations.py
│   │   └── courses.py
│   ├── services/
│   │   ├── course_service.py
│   │   └── message_service.py
│   ├── cache.py
│   ├── database.py
│   ├── dependencies.py
│   ├── jwt_security.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
├── test_db.py
├── test_pydantic.py
├── test_security.py
├── requirements.txt
├── .env
└── app.db
```

- `app/main.py` configure l'API FastAPI et enregistre les routes.
- `app/routes/` contient les routes d'authentification, de conversations et de cours.
- `app/services/` regroupe la logique métier des cours et des messages.
- `app/cache/` contient l'implémentation du cache Redis.
- `app/database.py`, `app/models.py` et `app/schemas.py` gèrent la base de données et les données de l'API.
- `app/security.py`, `app/jwt_security.py` et `app/dependencies.py` regroupent les fonctions de sécurité et les dépendances.
- `test_*.py` contient les tests du projet.
- `requirements.txt` liste les dépendances. `.env` contient la configuration locale et `app.db` est la base SQLite.

pip install fastapi uvicorn sqlalchemy


Lancer le serveur :
uvicorn app.main:app --reload

Ouvrir ensuite :

http://127.0.0.1:8000/db-test



<!-- Pour notre exemple avec FastAPI, nous allons utiliser pwdlib avec Argon2 et PyJWT pour les jetons JWT. -->
pip install "pwdlib[argon2]" pyjwt



Le fonctionnement complet de l'authentification
1. Inscription

L'utilisateur fournit son email et son mot de passe

2. Hachage

Le mot de passe est haché

3. Base de données

Enregistrement de l'utilisateur et du hachage

4. Connexion

Vérification de l'email et du mot de passe

5. JWT

Le serveur génère un jeton d'accès

6. Accès aux endpoints protégés

Le serveur vérifie le jeton avant d'autoriser l'accès


pip install redis

docker run --name redis-study-buddy -p 6379:6379 -d redis


Étape	Travail	Fichiers
1	Connexion SQLite	database.py
2	Modèles SQLAlchemy	models.py
3	Hashage des mots de passe	security.py
4	Schémas Pydantic	schemas.py
5	Inscription	routers/auth.py
6	Connexion et JWT	security.py, routers/auth.py
7	Identifier l'utilisateur connecté	dependencies.py
8	Créer une conversation	routers/conversations.py
9	Ajouter les messages utilisateur et assistant	routers/conversations.py
10	Protéger les conversations privées	routers/conversations.py
11	Ajouter un cache temporaire	Cache en mémoire
12	Rédiger le rapport	docs/security-persistence-report.md
13	Tester l'ensemble	Swagger / tests API