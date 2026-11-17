Explique la différence :
Fichier	Contenu	Partage
.env	Vraie clé API	Non
.env.example	Exemple sans secret	Oui

Installer les dépendances Python
Maintenant que les fichiers sont créés, nous allons installer les bibliothèques nécessaires.

Pour lire automatiquement le fichier .env, Python a besoin d'une bibliothèque appelée python-dotenv.

Nous allons également installer le SDK officiel OpenAI pour pouvoir communiquer avec son API.

Dans le terminal VS Code, exécuter :
pip install openai python-dotenv

installer gemini api : pip install google-genai python-dotenv

openai : permet d'utiliser le SDK OpenAI.



python-dotenv : permet de charger les variables enregistrées dans .env.

verifier installation
pip show openai
pip show python-dotenv


execute prg  -> python main.py


----------------------------------
Comprendre les trois rôles principaux
1. Le rôle system
Il définit le comportement de l'assistant.

Exemples :
- Tu es un professeur de Python.
- Tu réponds uniquement en français.
- Tu expliques avec des exemples simples.
- Tu ne donnes pas directement la solution aux exercices.
À expliquer : le message système sert à définir les règles générales de fonctionnement de l'assistant.
2. Le rôle user
Il représente les messages envoyés par l'utilisateur.

Exemples :
- Explique-moi les API.
- Donne-moi un exemple en Python.
- Quelle est la différence entre une liste et un dictionnaire ?
3. Le rôle assistant
Il représente les réponses générées par le modèle.

Exemple :

- Une API permet à différentes applications de communiquer entre elles.

Il permet également de conserver les réponses précédentes dans l'historique de conversation.
-----------------------------------
Cycle d'une requête IA

1- Créer les messages
Instructions système et question utilisateur


2- Envoyer la requête
Appel au SDK OpenAI


3- Recevoir la réponse
Le modèle retourne un objet réponse


4- Extraire le texte
Récupérer le contenu du message

5- Afficher le résultat
Afficher la réponse dans le terminal


------------
On utilise model au lieu de assistant, et parts au lieu de content
-----------
La température :
- 0.0 : réponses généralement plus déterministes.
- 0.3 : réponses plutôt cohérentes et structurées.
- 0.7 : réponses plus variées.
- 1.0 : davantage de créativité et de variation.
----------
Paramètre	Rôle	Exemple
model	Choisir le modèle IA	gemini-2.5-flash
temperature	Contrôler la créativité	0.3
max_output_tokens	Limiter la longueur de la réponse	800
system_instruction	Définir le comportement de l'assistant	Assistant pédagogique