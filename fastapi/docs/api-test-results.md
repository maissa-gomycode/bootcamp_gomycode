
# Résultats des tests API

## 1. GET /health

- Code HTTP attendu : 200
- Code HTTP obtenu : 200
- Résultat : Réussi
- Remarque : Le backend fonctionne correctement.

## 2. POST /chat - Message valide

- Code HTTP attendu : 200
- Code HTTP obtenu : 200
- Résultat : Réussi
- Remarque : Gemini retourne une réponse.

## 3. POST /chat - Message manquant

- Code HTTP attendu : 422
- Code HTTP obtenu : 422
- Résultat : Réussi
- Remarque : La validation détecte le champ manquant.

## 4. POST /chat - Message vide

- Code HTTP attendu : 400
- Code HTTP obtenu : 400
- Résultat : Réussi
- Remarque : Le backend refuse les espaces vides.

## 5. POST /chat - Message trop long

- Code HTTP attendu : 422
- Code HTTP obtenu : 422
- Résultat : Réussi
- Remarque : La limite de 2000 caractères est respectée.
