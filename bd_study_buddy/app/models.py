from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime, timezone
from app.database import Base

# ForeignKey() crée le lien au niveau de la base de données.
# relationship() permet de naviguer entre les objets Python.


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

     # Un utilisateur possède plusieurs conversations
    conversations = relationship(
        "Conversation",
        back_populates="user",
        cascade="all, delete-orphan"
    )

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    user = relationship(
        "User",
        back_populates="conversations"
    )

 # Une conversation possède plusieurs messages
    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan"
    )

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id"),
        nullable=False
    )

    role = Column(String, nullable=False)

    content = Column(Text, nullable=False)

    tokens_used = Column(Integer, default=0)

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )