class StubRepo:
    def __init__(self,exists=False):
        self._exists = exists

    def exists(self,user_email:str) -> bool:
        return self._exists

class StubRepoFactory:
    def get_factory(self,exists=False):
        return StubRepo(exists=exists)
