
# API Test Report

## 1. Objectif

Vérifier le fonctionnement des quatre endpoints
de notre backend FastAPI.

## 2. Résultats des tests manuels

| Endpoint | Scénario | Résultat attendu |
|---|---|---|
| GET /health | Requête valide | 200 |
| POST /chat | Message valide | 200 |
| POST /chat | Message manquant | 422 |
| POST /quiz | Sujet valide | 200 |
| POST /quiz | Sujet manquant | 422 |
| POST /quiz | Trop de questions | 422 |
| POST /summarise | Texte valide | 200 |
| POST /summarise | Texte trop court | 422 |

## 3. Résultats des tests automatisés

Commande utilisée :

python -m pytest -v

| Fichier | Scénario | Résultat |
|---|---|---|
| test_health.py | Vérification du statut | À compléter |
| test_chat.py | Message valide | À compléter |
| test_chat.py | Message manquant | À compléter |
| test_chat.py | Message vide | À compléter |
| test_quiz.py | Requête valide | À compléter |
| test_quiz.py | Trop de questions | À compléter |
| test_summarise.py | Requête valide | À compléter |

## 4. Erreurs de validation

### Chat

- Message manquant : HTTP 422.
- Message vide : HTTP 422.
- Message trop long : HTTP 422.

### Quiz

- Sujet manquant : HTTP 422.
- Nombre de questions supérieur à 10 : HTTP 422.

### Summarise

- Texte trop court : HTTP 422.
- Texte supérieur à 10 000 caractères : HTTP 422.
- Nombre de puces supérieur à 10 : HTTP 422.

## 5. Conclusion

Les tests permettent de vérifier que les endpoints
respectent les règles de validation et retournent
les structures JSON attendues.

Les résultats définitifs doivent être renseignés
après l'exécution réelle des tests.
