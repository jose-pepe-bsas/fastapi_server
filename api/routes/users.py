"""user api routers"""

from fastapi import FastAPI, Response, status
from fastapi import APIRouter
from pydantic import BaseModel

class RegisterUser(BaseModel):
    email:str
    password:str

user_route = APIRouter(prefix="/users")

@user_route.get("/")
async def root():
    return {}

@user_route.post("/signup/")
async def signup(register_user:RegisterUser, response:Response):
    if register_user.email.rstrip(" \n") == "" or register_user.password.rstrip(" \n") == "" :
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"sub":"Bad user data entries"}
    return {"sub":"user just register successfully"}

