from uuid import uuid4
from entities.user import User

class StubRepo:
    def __init__(self,exists=False):
        self._id:uuid4 = 0
        self._exists = exists
        self.password = None
        self.email = None

    def exists(self,user_email:str) -> bool:
        return self._exists 

    def with_pass(self,passw:str):
        self.password = passw
        return self

    def with_id(self,id:int):
        self._id = id 
        return self
    
    def get_id_by_email(self,email:str):
        if self._id == None:
            "email@gmail.com"
        return self._id

    def with_email(self,email:str):
        self._email = email 
        return self

    def get_user_by_id(self,id):
        return User(email=self._email,roles=2,password=self.password, id=self._id)

class StubRepoFactory:
    def get_factory(self,exists=False):
        return StubRepo(exists=exists)

