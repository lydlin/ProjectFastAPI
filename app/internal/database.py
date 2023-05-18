# Libs imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Chemin vers la base de données SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi.db"

# Création du moteur de base de données
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Création d'une session de base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe de base pour la déclaration des modèles
Base = declarative_base()
