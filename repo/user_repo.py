
class Repo:
    def __init__(self,db=[]):
        self._db = db

    def save(self,user=None,db=None):
        if db is None:
            db = self._db
        if user is not None:
            db.append(user)

    def exists(self,user_email:str,db=None) -> bool:
        if db is None:
            db = self._db
        for user in db:
            if user_email == user.email:
                return True
        return False

    def get_all(self,db=None) -> list:
        if db is None:
            db = self._db
        return db

    def get_id_by_email(self,email:str=None) -> str:
        if not email ==  None and self.exists(email):
            for user in self._db:
                if user.email == email:
                    return user.id 

