from pydantic import BaseModel

class SignUpUser(BaseModel):
    email:str
    password:str

