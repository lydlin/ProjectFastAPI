#System imports


#Libs imports
from fastapi import APIRouter, Response, status
from pydantic import BaseModel

#Local imports

router = APIRouter()

users = [
    {"id": 1, "name": "Léo"},
    {"id": 2, "name": "Yanis"},
    {"id": 3, "name": "Louis"},
    {"id": 4, "name": "Jacques"},
]

class User(BaseModel):
    id: int
    name: str

@router.get("/users", responses={status.HTTP_204_NO_CONTENT: {}})
async def get_all_users() -> list[User]:
    if len(users)==0:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return users

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User) -> User:
    for i in range(0, len(users)):
        if users[i]["id"] == user_id:
            users[i] = user.__dict__ 
    return Response(status_code = status.HTTP_200_OK)

