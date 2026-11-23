
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Conversation, User, Message

from app.schemas import (
    ConversationCreate,
    ConversationResponse,
    MessageCreate,
    MessageResponse
)

from app.dependencies import get_current_user
from app.services.message_service import save_message


router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)


# ==========================================
# 1. VERIFICATION DE PROPRIETE
# ==========================================

def get_user_conversation(
    conversation_id: int,
    current_user: User,
    db: Session
):
    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id
    ).first()

    if conversation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation introuvable"
        )

    return conversation


# ==========================================
# 2. CREER UNE CONVERSATION
# ==========================================

@router.post(
    "/",
    response_model=ConversationResponse,
    status_code=status.HTTP_201_CREATED
)
def create_conversation(
    conversation_data: ConversationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_conversation = Conversation(
        title=conversation_data.title,
        user_id=current_user.id
    )

    db.add(new_conversation)
    db.commit()
    db.refresh(new_conversation)

    return new_conversation


# ==========================================
# 3. CONSULTER SES CONVERSATIONS
# ==========================================

@router.get("/")
def get_my_conversations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    conversations = db.query(Conversation).filter(
        Conversation.user_id == current_user.id
    ).all()

    return conversations


# ==========================================
# 4. CONSULTER UNE CONVERSATION
# ==========================================

@router.get("/{conversation_id}")
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    conversation = get_user_conversation(
        conversation_id=conversation_id,
        current_user=current_user,
        db=db
    )

    return conversation


# ==========================================
# 5. AJOUTER UN MESSAGE
# ==========================================

@router.post(
    "/{conversation_id}/messages",
    response_model=list[MessageResponse]
)
def add_messages(
    conversation_id: int,
    message_data: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Vérifier que la conversation appartient à l'utilisateur
    conversation = get_user_conversation(
        conversation_id=conversation_id,
        current_user=current_user,
        db=db
    )

    # Enregistrer le message utilisateur
    user_message = save_message(
        db=db,
        conversation_id=conversation.id,
        role="user",
        content=message_data.content
    )

    # Réponse temporaire de l'assistant
    assistant_response = (
        "Merci pour votre message ! "
        "Je suis votre assistant Study Buddy."
    )

    # Enregistrer la réponse de l'assistant
    assistant_message = save_message(
        db=db,
        conversation_id=conversation.id,
        role="assistant",
        content=assistant_response
    )

    return [user_message, assistant_message]


# ==========================================
# 6. CONSULTER L'HISTORIQUE DES MESSAGES
# ==========================================

@router.get(
    "/{conversation_id}/messages",
    response_model=list[MessageResponse]
)
def get_conversation_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Vérifier la propriété de la conversation
    conversation = get_user_conversation(
        conversation_id=conversation_id,
        current_user=current_user,
        db=db
    )

    # Récupérer les messages
    messages = db.query(Message).filter(
        Message.conversation_id == conversation.id
    ).order_by(Message.created_at.asc()).all()

    return messages
