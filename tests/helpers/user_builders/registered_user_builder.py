from uuid import uuid4,UUID
from entities.user import RegisteredUser 

class RegisteredUserBuilder:
    def __init__(self,email:str="jose.s.contacto@gmail.com",
                 password:str="Password123",
                 roles:int=3,
                 id:str=str(uuid4())):
        self._email = email
        self._password = password
        self._roles = roles
        self._id = id

    def build(self):
        return RegisteredUser(email=self._email,
                    password=self._password,
                    roles=self._roles,
                    id=self._id)
