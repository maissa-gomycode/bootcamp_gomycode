
from sqlalchemy.orm import Session
from app.models import Message


def save_message(
    db: Session,
    conversation_id: int,
    role: str,
    content: str,
    tokens_used: int = 0
):
    message = Message(
        conversation_id=conversation_id,
        role=role,
        content=content,
        tokens_used=tokens_used
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message
