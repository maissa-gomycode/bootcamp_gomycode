from app.schemas import UserCreate, UserResponse

# Test avec un email valide
user = UserCreate(
    email="maissa@example.com",
    password="MonMotDePasse123"
)

print(user)

# Test avec un email invalide
try:
    UserCreate(
        email="maissa",
        password="123456"
    )
    print(UserResponse.model_fields.keys())
except Exception as e:
    print("Erreur de validation :", e)