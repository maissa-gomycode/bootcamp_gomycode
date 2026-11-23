
from app.security import hash_password, verify_password

password = "MonMotDePasse123"

# Hacher le mot de passe
hashed = hash_password(password)

print("Mot de passe haché :")
print(hashed)

# Vérifier le bon mot de passe
print("Vérification du bon mot de passe :")
print(verify_password(password, hashed))

# Vérifier un mauvais mot de passe
print("Vérification d'un mauvais mot de passe :")
print(verify_password("123456", hashed))
