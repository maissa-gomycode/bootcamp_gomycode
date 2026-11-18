
from fastapi import APIRouter

from app.schemas.requests import ChatRequest
from app.services.chat_service import generate_chat_response

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)


@router.post("")
def chat(request: ChatRequest):

    result = generate_chat_response(
        request.message
    )

    return result
