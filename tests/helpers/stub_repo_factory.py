class StubRepo:
    def __init__(self,exists=False):
        self._id = 0
        self._exists = exists

    def exists(self,user_email:str) -> bool:
        return self._exists 

    def with_id(self,id:int):
        self._id = id 
        return self

class StubRepoFactory:
    def get_factory(self,exists=False):
        return StubRepo(exists=exists)
