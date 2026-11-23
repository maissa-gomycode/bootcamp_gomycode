# JWT est un format de jeton utilisé pour transmettre des informations permettant notamment de gérer l'authentification.

from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY = "REMPLACER_PAR_UN_SECRET_LONG_ET_ALEATOIRE"

ALGORITHM = "HS256"


def create_access_token(user_id: int):

    # Date d'expiration : 30 minutes
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    # Informations à intégrer dans le jeton
    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    # Générer le JWT
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token