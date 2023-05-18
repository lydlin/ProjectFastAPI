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

# Récupérer toutes les entreprises
@router.get("/entreprises/", response_model=list[schemas.Entreprise])
def get_all_entreprises(db: Session = Depends(get_db)):
    entreprises = db.query(models.Entreprise).all()
    return entreprises

# Récupérer une entreprise par son ID
@router.get("/entreprise/{entreprise_id}", response_model=schemas.Entreprise)
def get_entreprise(entreprise_id: int, db: Session = Depends(get_db)):
    db_entreprise = db.query(models.Entreprise).filter(models.Entreprise.id == entreprise_id).first()
    if not db_entreprise:
        raise HTTPException(status_code=404, detail="Entreprise non trouvée")
    return db_entreprise

# Créer une entreprise
@router.post("/entreprise/", response_model=schemas.Entreprise)
def create_entreprise(entreprise: schemas.EntrepriseCreate, db: Session = Depends(get_db)):
    db_entreprise = models.Entreprise(nom=entreprise.nom)
    db.add(db_entreprise)
    db.commit()
    db.refresh(db_entreprise)
    return db_entreprise

# Mettre à jour une entreprise
@router.put("/entreprise/{entreprise_id}", response_model=schemas.Entreprise)
def update_entreprise(entreprise_id: int, entreprise: schemas.EntrepriseUpdate, db: Session = Depends(get_db)):
    db_entreprise = db.query(models.Entreprise).filter(models.Entreprise.id == entreprise_id).first()
    if not db_entreprise:
        raise HTTPException(status_code=404, detail="Entreprise non trouvée")
    db_entreprise.nom = entreprise.nom
    db.commit()
    db.refresh(db_entreprise)
    return db_entreprise

# Supprimer une entreprise
@router.delete("/entreprise/{entreprise_id}")
def delete_entreprise(entreprise_id: int, db: Session = Depends(get_db)):
    db_entreprise = db.query(models.Entreprise).filter(models.Entreprise.id == entreprise_id).first()
    if not db_entreprise:
        raise HTTPException(status_code=404, detail="Entreprise non trouvée")
    db.delete(db_entreprise)
    db.commit()
    return {"message": "Entreprise supprimée"}