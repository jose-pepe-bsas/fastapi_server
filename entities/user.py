from pydantic import BaseModel
import uuid

class User(BaseModel):
    email:str
    password:str
    roles:int 
    id:None | uuid.UUID

