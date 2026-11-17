
# Gemini Terminal Assistant

## Description

Assistant IA conversationnel développé avec Python
et l'API Google Gemini.

Il permet de poser des questions en langage naturel
et de recevoir des réponses directement dans le terminal.

## Fonctionnalités

- Connexion à l'API Gemini
- Clé API protégée dans un fichier .env
- Instructions système personnalisées
- Conversation avec historique
- Commandes help, clear, exit et quit
- Affichage de l'utilisation des jetons
- Gestion des erreurs API

## Technologies

- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv

## Installation

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Configuration

Créer un fichier .env à la racine du projet :

GEMINI_API_KEY=votre_cle_api

## Exécution

```bash
python main.py
```

## Exemple d'utilisation

Vous : Qu'est-ce qu'une API REST ?

Gemini : Une API REST permet à deux applications
de communiquer via HTTP.

Vous : Donne-moi un exemple.

Gemini : Une application météo qui récupère
les prévisions depuis un serveur.

## Commandes

- help : afficher les commandes
- clear : réinitialiser la conversation
- quit : quitter
- exit : quitter
