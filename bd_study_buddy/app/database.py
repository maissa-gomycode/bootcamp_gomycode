from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Adresse de notre base de données SQLite
DATABASE_URL = "sqlite:///./app.db"

# Création du moteur de connexion
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Création des sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe de base des modèles
Base = declarative_base()


# Fonction qui fournit une session à FastAPI
def get_db():
    db = SessionLocal()

    try:
        # met la session à disposition de l'endpoint.
        yield db
    # garantit la fermeture de la session à la fin de son utilisation.
    finally:
        db.close()