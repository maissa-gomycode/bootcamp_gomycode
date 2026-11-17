SYSTEM_PROMPT = """
Tu es un assistant pédagogique.

Ton rôle est d'aider les étudiants
à comprendre les concepts informatiques.

Règles :
- Explique clairement et simplement.
- Utilise des exemples pratiques.
- Réponds en français.
- Si tu ne connais pas une réponse,
  indique que tu n'es pas sûr.
"""

# Créer la liste des messages
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": "Qu'est-ce qu'une API ?"
    },
    {
        "role": "assistant",
        "content": "Un dictionnaire stocke des données sous forme de clés et de valeurs."
    },
    {
        "role": "user",
        "content": "Donne-moi un exemple."
    }
]