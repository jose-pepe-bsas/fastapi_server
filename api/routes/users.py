"""user api routers"""

from fastapi import FastAPI, Response, status, Request
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Annotated
from entities.authuser import AuthUser
from servicios.account.signup import SignUp
from servicios.account.login import Login
from repo.user_repo import Repo
from entities.trySignUpUser import SignUpUser 
from fastapi.responses import JSONResponse
from fastapi import Header
from servicios.tokens.token_validator import TokenValidator
from servicios.tokens.read_token import TokenReader
from servicios.account.login import CurrentActiveUsers
from servicios.envkeysgen import generate_env_key_value,set_key
from servicios.account.auth import Auth


KEY = generate_env_key_value()
set_key("AUTH_TOKEN_KEY", KEY)

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
    credential = Login().log_user_in(user_email=auth_user.email,
                        user_password=auth_user.password,
                        db=db,active_list=active_list)
    auth_token = credential['access_token']
    refresh_token = credential['refresh_token']
    response.headers['auth_token'] = auth_token
    response.headers['refresh_token'] = refresh_token
    headers = {
        'auth_token' : auth_token,
        'refresh_token' : refresh_token}
    return JSONResponse(content=headers,headers=headers)

token_reader = TokenReader()
token_validator = TokenValidator()

@user_route.get("/user/{user_id}")
async def get_profile(user_id:str,token: Annotated[str | None, Header()],request:Request):
    access_token = request.headers.get("token")
    if not Auth().ask_access(user_token=access_token,
                         token_reader=token_reader,
                         token_validator=token_validator,
                         logged_users=active_list):
        return "Usted no tiene una sesion autorizada"
    else:

        if Auth().profile_owner(user_token=access_token,
                                token_reader=token_reader,
                                profile_id=user_id
                                ):
                                
            return "Accedio"
        else:
            return "Fuera bastardo xd"
