from pydantic import BaseModel

class RegisterUser(BaseModel):
    email:str
    password:str

