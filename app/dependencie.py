# Local imports
from internal.database import SessionLocal

# Fonction utilitaire pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
