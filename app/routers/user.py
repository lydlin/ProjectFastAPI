# System imports
from typing import Annotated
import datetime
# Libs imports
from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

# Local imports
from internal import models
from internal import schemas
from dependencie import get_db

router = APIRouter()

# Récupérer tous les utilisateurs
@router.get("/users/", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
# Récupérer un utilisateur par son ID
@router.get("/user/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return db_user

# Créer un utilisateur
@router.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(
        nom=user.nom,
        prenom=user.prenom,
        email=user.email,
        mdp=user.mdp,
        id_entreprise=user.id_entreprise,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Mettre à jour un utilisateur
@router.put("/user/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    db_user.nom = user.nom
    db_user.prenom = user.prenom
    db_user.email = user.email
    db_user.mdp = user.mdp
    db_user.id_entreprise = user.id_entreprise
    db_user.role = user.role
    db.commit()
    db.refresh(db_user)
    return db_user


# Supprimer un utilisateur
@router.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    db.delete(db_user)
    db.commit()
    return {"message": "Utilisateur supprimé"}