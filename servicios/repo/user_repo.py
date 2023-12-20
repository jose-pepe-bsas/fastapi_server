
class Repo:
    def __init__(self,db=[]):
        self._db = db

    def save(self,user=None):
        if user is not None:
            self._db.append(user)

    def exists(self,user_email:str) -> bool:
        for user in self._db:
            if user_email == user.email:
                return True
        return False


