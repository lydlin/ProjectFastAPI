#System imports


#Libs imports
from fastapi import FastAPI, status, Depends

#Local imports
from routers import user

app = FastAPI()

@app.get("/")
async def say_hello():
    """Projet Fullstack back
    """
    return "Hello"


app.include_router(user.router, tags=["users"])
