
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.ai import call_llm

# Création du routeur
router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

# Modèle de requête
class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000
    )

# Modèle de réponse
class ChatResponse(BaseModel):
    answer: str
    model: str
    tokens_used: int

# Endpoint POST /chat
@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):

    clean_message = request.message.strip()

    if not clean_message:
        raise HTTPException(
            status_code=400,
            detail="Le message ne peut pas être vide."
        )

    try:
        result = call_llm(clean_message)

        return ChatResponse(**result)

    except RuntimeError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error)
        )
