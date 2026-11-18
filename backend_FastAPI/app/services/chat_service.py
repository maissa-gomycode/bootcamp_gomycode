
def generate_chat_response(message: str) -> dict:

    answer = (
        f"Votre message a bien été reçu : {message}. "
        "Je suis votre assistant d'apprentissage."
    )

    return {
        "answer": answer,
        "model": "basic-logic",
        "tokens_used": len(message.split())
    }
