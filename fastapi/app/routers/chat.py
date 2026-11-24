
# ==================================================
# IMPORTATIONS
# ==================================================

import asyncio

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.ai import (
    generate_ai_response,
    generate_summary,
    generate_quiz,
    generate_flashcards
)


# ==================================================
# CRÉATION DU ROUTEUR
# ==================================================

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)


# ==================================================
# MODÈLE DE REQUÊTE CHAT
# ==================================================

class ChatRequest(BaseModel):

    message: str = Field(
        ...,
        min_length=1,
        max_length=2000
    )


# ==================================================
# MODÈLE DE RÉPONSE CHAT
# ==================================================

class ChatResponse(BaseModel):

    answer: str
    model: str
    tokens_used: int


# ==================================================
# MODÈLE DE REQUÊTE STUDY PACK
# ==================================================

class StudyPackRequest(BaseModel):

    content: str = Field(
        ...,
        min_length=1,
        max_length=10000
    )


# ==================================================
# ENDPOINT POST /chat
# ==================================================

@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):

    clean_message = request.message.strip()

    if not clean_message:

        raise HTTPException(
            status_code=400,
            detail="Le message ne peut pas être vide."
        )

    try:

        # Appel asynchrone du service IA
        result = await generate_ai_response(clean_message)

        return ChatResponse(**result)

    except TimeoutError as error:

        raise HTTPException(
            status_code=504,
            detail=str(error)
        )

    except RuntimeError as error:

        raise HTTPException(
            status_code=503,
            detail=str(error)
        )


# ==================================================
# ENDPOINT POST /chat/study-pack
# ==================================================

@router.post("/study-pack")
async def create_study_pack(request: StudyPackRequest):

    content = request.content.strip()

    if not content:

        raise HTTPException(
            status_code=400,
            detail="Le contenu du cours ne peut pas être vide."
        )

    try:

        # Exécution concurrente des trois tâches
        summary, quiz, flashcards = await asyncio.gather(

            generate_summary(content),

            generate_quiz(content),

            generate_flashcards(content)

        )

        return {
            "success": True,
            "study_pack": {
                "summary": summary,
                "quiz": quiz,
                "flashcards": flashcards
            }
        }

    except TimeoutError as error:

        raise HTTPException(
            status_code=504,
            detail=str(error)
        )

    except RuntimeError as error:

        raise HTTPException(
            status_code=503,
            detail=str(error)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Une erreur inattendue est survenue."
        )
