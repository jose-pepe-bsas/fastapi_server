"""user api routers"""

from fastapi import FastAPI, Response, status
from fastapi import APIRouter
from pydantic import BaseModel
from entities.authuser import AuthUser
from servicios.account.signup import SignUp
from servicios.account.login import Login
from repo.user_repo import Repo
from entities.trySignUpUser import SignUpUser 
from fastapi import Header
from servicios.account.login import CurrentActiveUsers

user_route = APIRouter(prefix="/users")

db = Repo()
active_list = CurrentActiveUsers()


@user_route.get("/")
async def root():
    return db.get_all()

@user_route.post("/signup/")
async def signup(register_user:SignUpUser, response:Response):
    if register_user.email.rstrip(" \n") == "" or register_user.password.rstrip(" \n") == "" :
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"sub":"Bad user data entries"}
    SignUp().create_user(user=register_user,db=db)
    return {"sub":"user just register successfully"}




@user_route.post("/login/")
async def login(auth_user:AuthUser, response:Response):
    if auth_user.email.rstrip(" \n") == "" or auth_user.password.rstrip(" \n") == "" :
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"sub":"Bad user data entries"}
    auth_token,refresh_token = Login().log_user_in(user_email=auth_user.email,
                        user_password=auth_user.password,
                        db=db,active_list=active_list)
    response.headers['auth_token'] = auth_token
    response.headers['refresh_token'] = refresh_token
                

    return {"sub": "user just register successfully"}



