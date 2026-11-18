
from pydantic import BaseModel, Field, field_validator


# ==========================================
# CHAT
# ==========================================

class ChatRequest(BaseModel):

    message: str = Field(
        ...,
        min_length=1,
        max_length=2000
    )

    @field_validator("message")
    @classmethod
    def validate_message(cls, value):
        if not value.strip():
            raise ValueError("Le message ne peut pas être vide.")
        return value.strip()


# ==========================================
# QUIZ
# ==========================================

class QuizRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    num_questions: int = Field(
        default=5,
        ge=1,
        le=10
    )

    @field_validator("topic")
    @classmethod
    def validate_topic(cls, value):
        if not value.strip():
            raise ValueError("Le sujet ne peut pas être vide.")
        return value.strip()


# ==========================================
# SUMMARISE
# ==========================================

class SummariseRequest(BaseModel):

    text: str = Field(
        ...,
        min_length=10,
        max_length=10000
    )

    max_bullets: int = Field(
        default=3,
        ge=1,
        le=10
    )

    @field_validator("text")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("Le texte ne peut pas être vide.")
        return value.strip()
