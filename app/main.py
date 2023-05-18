# Libs imports
from fastapi import FastAPI, HTTPException, Depends

# Local imports
from internal import models
from internal.database import engine
from routers import activite, entreprise, planning, user, inscription

app = FastAPI()

# Création des tables dans la base de données
models.Base.metadata.create_all(bind=engine)

app.include_router(user.router, tags=["User"])
app.include_router(entreprise.router, tags=["Entreprise"])
app.include_router(planning.router, tags=["Planning"])
app.include_router(activite.router, tags=["Activités"])
app.include_router(inscription.router, tags=["Inscription Activité"])