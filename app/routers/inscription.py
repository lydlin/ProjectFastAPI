# System imports
from typing import List
from datetime import datetime

# Libs imports
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

# Local imports
from internal import models, schemas
from dependencie import get_db

router = APIRouter()


# Récupérer toutes les inscriptions
@router.get("/inscriptions/", response_model=List[schemas.Inscription])
def get_all_inscriptions(db: Session = Depends(get_db)):
    inscriptions = db.query(models.Inscription).all()
    return inscriptions


# Récupérer une inscription par son ID
@router.get("/inscription/{inscription_id}", response_model=schemas.Inscription)
def get_inscription(inscription_id: int, db: Session = Depends(get_db)):
    db_inscription = db.query(models.Inscription).filter(models.Inscription.id_Inscription == inscription_id).first()
    if not db_inscription:
        raise HTTPException(status_code=404, detail="Inscription non trouvée")
    return db_inscription


# Créer une inscription
@router.post("/inscription/", response_model=schemas.Inscription)
def create_inscription(inscription: schemas.InscriptionCreate, db: Session = Depends(get_db)):
    db_inscription = models.Inscription(
        id_activite=inscription.id_activite,
        id_user=inscription.id_user
    )
    db.add(db_inscription)
    db.commit()
    db.refresh(db_inscription)
    return db_inscription


# Mettre à jour une inscription
@router.put("/inscription/{inscription_id}", response_model=schemas.Inscription)
def update_inscription(inscription_id: int, inscription: schemas.InscriptionUpdate, db: Session = Depends(get_db)):
    db_inscription = db.query(models.Inscription).filter(models.Inscription.id_Inscription == inscription_id).first()
    if not db_inscription:
        raise HTTPException(status_code=404, detail="Inscription non trouvée")
    db_inscription.id_activite = inscription.id_activite
    db_inscription.id_user = inscription.id_user
    db.commit()
    db.refresh(db_inscription)
    return db_inscription


# Supprimer une inscription
@router.delete("/inscription/{inscription_id}")
def delete_inscription(inscription_id: int, db: Session = Depends(get_db)):
    db_inscription = db.query(models.Inscription).filter(models.Inscription.id_Inscription == inscription_id).first()
    if not db_inscription:
        raise HTTPException(status_code=404, detail="Inscription non trouvée")
    db.delete(db_inscription)
    db.commit()
    return {"message": "Inscription supprimée"}
