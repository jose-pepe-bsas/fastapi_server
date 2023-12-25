from pydantic import BaseModel

class AuthUser(BaseModel):
    email:str
    password:str
