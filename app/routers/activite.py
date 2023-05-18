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

# Récupérer toutes les activités
@router.get("/activites/", response_model=list[schemas.Activite])
def get_all_activites(db: Session = Depends(get_db)):
    activites = db.query(models.Activite).all()
    return activites

# Récupérer une activité par son ID
@router.get("/activite/{activite_id}", response_model=schemas.Activite)
def get_activite(activite_id: int, db: Session = Depends(get_db)):
    db_activite = db.query(models.Activite).filter(models.Activite.id == activite_id).first()
    if not db_activite:
        raise HTTPException(status_code=404, detail="Activité non trouvée")
    return db_activite

# Créer une activité
@router.post("/activite/", response_model=schemas.Activite)
def create_activite(activite: schemas.ActiviteCreate, db: Session = Depends(get_db)):
    db_activite = models.Activite(
        nom=activite.nom,
        lieu=activite.lieu,
        date_debut=activite.date_debut,
        date_fin=activite.date_fin,
        id_planning=activite.id_planning,
        id_createur=activite.id_createur,
        nbr_participant=activite.nbr_participant
    )
    db.add(db_activite)
    db.commit()
    db.refresh(db_activite)
    return db_activite

# Mettre à jour une activité
@router.put("/activite/{activite_id}", response_model=schemas.Activite)
def update_activite(activite_id: int, activite: schemas.ActiviteUpdate, db: Session = Depends(get_db)):
    db_activite = db.query(models.Activite).filter(models.Activite.id == activite_id).first()
    if not db_activite:
        raise HTTPException(status_code=404, detail="Activité non trouvée")
    db_activite.nom = activite.nom
    db_activite.lieu = activite.lieu
    db_activite.date_debut = activite.date_debut
    db_activite.date_fin = activite.date_fin
    db_activite.id_planning = activite.id_planning
    db_activite.id_createur = activite.id_createur
    db_activite.nbr_participant = activite.nbr_participant
    db.commit()
    db.refresh(db_activite)
    return db_activite


# Supprimer une activité
@router.delete("/activite/{activite_id}")
def delete_activite(activite_id: int, db: Session = Depends(get_db)):
    db_activite = db.query(models.Activite).filter(models.Activite.id == activite_id).first()
    if not db_activite:
        raise HTTPException(status_code=404, detail="Activité non trouvée")
    db.delete(db_activite)
    db.commit()
    return {"message": "Activité supprimée"}