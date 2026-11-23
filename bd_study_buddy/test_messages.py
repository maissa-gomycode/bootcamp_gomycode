from app.database import SessionLocal
from app.models import Message

db = SessionLocal()

messages = db.query(Message).all()

for message in messages:
    print("-----------------------")
    print("ID :", message.id)
    print("Conversation :", message.conversation_id)
    print("Rôle :", message.role)
    print("Contenu :", message.content)

db.close()