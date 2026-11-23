from app.database import SessionLocal
from app.models import User, Conversation, Message

db = SessionLocal()

print("Users:", db.query(User).count())
print("Conversations:", db.query(Conversation).count())
print("Messages:", db.query(Message).count())

db.close()