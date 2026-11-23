
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse, UserLogin, TokenResponse
from app.security import hash_password, verify_password, create_access_token

# Le router: ous les endpoints de ce fichier commenceront par /auth.
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# =================================
# REGISTER
# =================================

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    # 1. Vérifier si l'email existe déjà
    email = str(user.email).strip().lower()

    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cet email est déjà utilisé."
        )

    # 2. Hasher le mot de passe
    hashed_password = hash_password(user.password)

    # 3. Créer le nouvel utilisateur
    new_user = User(
        email=email,
        password_hash=hashed_password
    )

    # 4. Enregistrer dans SQLite
    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cet email est déjà utilisé."
        )

    # 5. Retourner les informations publiques
    return new_user



# =================================
# LOGIN
# =================================

@router.post(
    "/login",
    response_model=TokenResponse
)
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    # 1. Rechercher l'utilisateur
    email = str(user.email).strip().lower()

    db_user = db.query(User).filter(
        User.email == email
    ).first()

    # 2. Vérifier l'utilisateur et son mot de passe
    if not db_user or not verify_password(
        user.password,
        db_user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Email ou mot de passe incorrect."
        )

    # 3. Générer le JWT
    access_token = create_access_token(
        data={"sub": str(db_user.id)}
    )

    # 4. Retourner le token
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
