
from fastapi import APIRouter

from app.schemas.requests import QuizRequest
from app.services.quiz_service import generate_quiz

router = APIRouter(
    prefix="/quiz",
    tags=["quiz"]
)


@router.post("")
def quiz(request: QuizRequest):

    result = generate_quiz(
        topic=request.topic,
        num_questions=request.num_questions
    )

    return result
