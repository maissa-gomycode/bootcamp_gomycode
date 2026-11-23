
# 📚 Study Buddy – Assistant d'étude avec Mistral AI

## 1. Présentation du projet

Study Buddy est un assistant d'étude développé en Python qui utilise l'API Mistral AI.

Il permet aux étudiants de poser des questions, de comprendre des notions et de recevoir des explications pédagogiques.

L'assistant conserve l'historique de la conversation afin de pouvoir utiliser les échanges précédents comme contexte.

## 2. Structure du projet

```text
study_buddy/
│
├── study_buddy.py
├── .env
├── .gitignore
└── README.md
```

## 3. Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python 3.10 ou supérieur.
- Une clé API Mistral valide.

## 4. Installation des bibliothèques

Ouvrir le terminal dans le dossier du projet et exécuter :

```bash
pip install mistralai python-dotenv openai
```

### Rôle des bibliothèques

- **mistralai** : permet de communiquer avec l'API Mistral.
- **python-dotenv** : permet de charger les variables d'environnement depuis le fichier `.env`, notamment la clé API.
- **openai** : permet d'utiliser le client OpenAI compatible avec l'API Mistral (option bonus).

### Vérifier l'installation

```bash
pip show mistralai
```

## 5. Configuration de la clé API

Créer un fichier nommé `.env` à la racine du projet.

Ajouter votre clé API :

```env
MISTRAL_API_KEY=votre_cle_api_ici
```

**Important :** Remplacer `votre_cle_api_ici` par votre véritable clé API Mistral.

Ne jamais partager cette clé ou l'écrire directement dans le code Python.

## 6. Sécurisation avec .gitignore

Créer un fichier `.gitignore` et ajouter :

```gitignore
.env
__pycache__/
*.pyc
.venv/
venv/
```

Cela permet d'éviter l'envoi du fichier contenant la clé API sur GitHub.

## 7. Exécution du projet

### Mode natif Mistral

Pour lancer l'assistant avec le SDK Mistral :

```bash
python study_buddy.py
```

### Mode compatible OpenAI (option bonus)

Pour utiliser le client OpenAI avec le point de terminaison compatible Mistral :

```bash
python study_buddy.py --openai
```

## 8. Fonctionnalités principales

- **Message système (System Prompt)** : définit la personnalité et le rôle de l'assistant.
- **Messages et rôles** : distingue les messages du système, de l'utilisateur et de l'assistant.
- **Mémoire de conversation** : conserve les échanges précédents dans une liste `messages`.
- **Température** : utilise une valeur de `0.3` pour obtenir des réponses relativement stables.
- **Max Tokens** : limite la longueur des réponses générées.
- **Gestion des erreurs** : utilise `try/except` pour gérer les erreurs API et réseau.
- **Portabilité** : permet d'utiliser le SDK Mistral ou le client OpenAI compatible.

## 9. Exemple de conversation

```text
Bienvenue dans Study Buddy !

Étudiant : Je veux apprendre Python. Qu'est-ce qu'une variable ?

Study Buddy : Une variable est un espace qui permet de stocker une information.
Par exemple : nom = "Ali".

Étudiant : Peux-tu me donner un autre exemple ?

Study Buddy : Bien sûr ! Par exemple : age = 20.

Étudiant : Comment afficher cette valeur ?

Study Buddy : Tu peux utiliser print(age) pour afficher la valeur 20.

Étudiant : quit

Study Buddy : Bon courage pour tes études ! À bientôt.
```

## 10. Tester la mémoire de conversation

Pour vérifier que l'assistant conserve le contexte :

1. Demander une explication sur les variables Python.
2. Demander un autre exemple sans répéter le sujet.
3. Demander comment afficher la valeur évoquée précédemment.

L'assistant doit comprendre les questions suivantes grâce à l'historique de conversation.

## 11. Sécurité

- Ne jamais écrire la clé API directement dans le code.
- Ne jamais envoyer le fichier `.env` sur GitHub.
- Ne jamais partager sa clé API avec une autre personne.
- Vérifier que `.env` figure bien dans `.gitignore`.

---

**Projet : Study Buddy**

**Technologies :** Python, Mistral AI API, mistralai, python-dotenv, OpenAI SDK.
