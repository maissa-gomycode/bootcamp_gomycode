
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Literal
from pydantic import Field

# =================================
# USER SCHEMAS
# =================================

# Données reçues lors de l'inscription
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


# Données retournées après inscription
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# =================================
# AUTHENTICATION SCHEMAS
# =================================

# Données reçues lors de la connexion
class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


# Réponse contenant le JWT
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# =================================
# CONVERSATION SCHEMAS
# =================================

# Données reçues pour créer une conversation
class ConversationCreate(BaseModel):
    title: str


# Données retournées pour une conversation
class ConversationResponse(BaseModel):
    id: int
    title: str
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# =================================
# MESSAGE SCHEMAS
# =================================

# Données reçues pour envoyer un message
class MessageCreate(BaseModel):
    content: str


# Données retournées pour un message
class MessageResponse(BaseModel):
    id: int
    conversation_id: int
    role: Literal["user", "assistant"]
    content: str
    created_at: datetime
    tokens_used: int
    model_config = ConfigDict(from_attributes=True)
