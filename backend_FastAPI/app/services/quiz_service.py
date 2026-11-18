
def generate_quiz(topic: str, num_questions: int) -> dict:

    questions = []

    for i in range(1, num_questions + 1):

        questions.append({
            "id": i,
            "question": f"Question {i} : Que savez-vous sur {topic} ?",
            "options": [
                "Option A",
                "Option B",
                "Option C"
            ]
        })

    return {
        "topic": topic,
        "total_questions": len(questions),
        "questions": questions
    }
