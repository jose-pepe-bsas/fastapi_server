class StubRepo:
    def __init__(self,exists=False):
        self._id = 0
        self._exists = exists

    def exists(self,user_email:str) -> bool:
        return self._exists 

    def with_id(self,id:int):
        self._id = id 
        return self
    
    def get_id_by_email(self,email:str):
        if self._id == None:
            "email@gmail.com"
        return self._id

class StubRepoFactory:
    def get_factory(self,exists=False):
        return StubRepo(exists=exists)

