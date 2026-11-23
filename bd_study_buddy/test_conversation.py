from app.database import SessionLocal
from app.models import Conversation

db = SessionLocal()

conversations = db.query(Conversation).all()

for conversation in conversations:
    print("ID :", conversation.id)
    print("Titre :", conversation.title)
    print("Utilisateur :", conversation.user_id)

db.close()