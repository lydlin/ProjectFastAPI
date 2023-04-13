#System imports

#Libs imports
from fastapi import FastAPI, Response, status

#Local imports
from routers import cars, users
from internal import auth

app = FastAPI()

app.include_router(auth.router, tags=["Authentification"])
app.include_router(cars.router, tags=["Car"])
app.include_router(users.router, tags=["User"])
