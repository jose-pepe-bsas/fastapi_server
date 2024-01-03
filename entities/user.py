from pydantic import BaseModel

class RegisteredUser(BaseModel):
    email:str
    roles:int 
    password:str
    id:None | str

