
from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter(
    tags=["health"]
)


@router.get("/health")
def health():

    return {
        "status": "ok",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
