
from fastapi import APIRouter

from app.schemas.requests import SummariseRequest
from app.services.summarise_service import generate_summary

router = APIRouter(
    prefix="/summarise",
    tags=["summarise"]
)


@router.post("")
def summarise(request: SummariseRequest):

    result = generate_summary(
        text=request.text,
        max_bullets=request.max_bullets
    )

    return result
