"""user api routers"""

from fastapi import FastAPI, Response, status
from fastapi import APIRouter
from pydantic import BaseModel
from servicios.signup import SignUp
from servicios.repo.user_repo import Repo
from entities.trySignUpUser import RegisterUser

user_route = APIRouter(prefix="/users")

db = Repo()

class AuthUser(BaseModel):
    email:str
    password:str

@user_route.get("/")
async def root():
    return db.get_all()

@user_route.post("/signup/")
async def signup(register_user:RegisterUser, response:Response):
    if register_user.email.rstrip(" \n") == "" or register_user.password.rstrip(" \n") == "" :
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"sub":"Bad user data entries"}
    SignUp().create_user(user=register_user,db=db)
    return {"sub":"user just register successfully"}


