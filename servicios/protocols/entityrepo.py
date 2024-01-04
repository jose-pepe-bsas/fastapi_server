from abc import ABC, abstractmethod
class ENTITY_REPO(ABC):

    @abstractmethod
    def save(self,user=None,db=None):
        pass

    @abstractmethod
    def exists(self,user_email:str,db=None) -> bool:
        pass

    @abstractmethod
    def get_all(self,db=None) -> list:
        pass
