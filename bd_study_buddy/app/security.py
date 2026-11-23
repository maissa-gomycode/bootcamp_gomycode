from pwdlib import PasswordHash
from jose import jwt
from datetime import datetime, timedelta, timezone
import os

# Configuration du hachage
password_hash = PasswordHash.recommended()

SECRET_KEY = "REMPLACER_PAR_UN_SECRET_LONG_ET_ALEATOIRE"

ALGORITHM = "HS256"

# Transformer un mot de passe en hachage

def hash_password(password: str) -> str:
    return password_hash.hash(password)

# Vérifier le mot de passe
def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password
    )


# =================================
# JWT CONFIGURATION
# =================================

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError(
        "SECRET_KEY n'est pas configurée."
    )

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


# =================================
# CREATE ACCESS TOKEN
# =================================

def create_access_token(data: dict) -> str:

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt
