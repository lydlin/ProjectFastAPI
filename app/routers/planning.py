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

# Récupérer tous les plannings
@router.get("/plannings/", response_model=list[schemas.Planning])
def get_all_plannings(db: Session = Depends(get_db)):
    plannings = db.query(models.Planning).all()
    return plannings

# Récupérer un planning par son ID
@router.get("/planning/{planning_id}", response_model=schemas.Planning)
def get_planning(planning_id: int, db: Session = Depends(get_db)):
    db_planning = db.query(models.Planning).filter(models.Planning.id == planning_id).first()
    if not db_planning:
        raise HTTPException(status_code=404, detail="Planning non trouvé")
    return db_planning

# Créer un planning
@router.post("/planning/", response_model=schemas.Planning)
def create_planning(planning: schemas.PlanningCreate, db: Session = Depends(get_db)):
    db_planning = models.Planning(
        nom=planning.nom,
        id_entreprise=planning.id_entreprise
    )
    db.add(db_planning)
    db.commit()
    db.refresh(db_planning)
    return db_planning

# Mettre à jour un planning
@router.put("/planning/{planning_id}", response_model=schemas.Planning)
def update_planning(planning_id: int, planning: schemas.PlanningUpdate, db: Session = Depends(get_db)):
    db_planning = db.query(models.Planning).filter(models.Planning.id == planning_id).first()
    if not db_planning:
        raise HTTPException(status_code=404, detail="Planning non trouvé")
    db_planning.nom = planning.nom
    db_planning.id_entreprise = planning.id_entreprise
    db.commit()
    db.refresh(db_planning)
    return db_planning


# Supprimer un planning
@router.delete("/planning/{planning_id}")
def delete_planning(planning_id: int, db: Session = Depends(get_db)):
    db_planning = db.query(models.Planning).filter(models.Planning.id == planning_id).first()
    if not db_planning:
        raise HTTPException(status_code=404, detail="Planning non trouvé")
    db.delete(db_planning)
    db.commit()
    return {"message": "Planning supprimé"}