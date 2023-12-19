"""Modulo de repo de usuarios"""

class Repo:
    def __init__(self,db=[]):
        self._db = db

    def save(self,user=None):
        if user is not None:
            self._db.append(user)

    def exists(self,user_email:str) -> bool:
        for user in self._db:
            if user_email == user["email"]:
                return True
        return False


def test_serv_should_know_if_a_user_exists_or_not():
    sut = Repo(db=[])
    sut.save(user={"email":"jose.s.contacto@gmail.com"})
    assert sut.exists(user_email="jose.s.contacto@gmail.com")
    assert sut.exists(user_email="manolo@gmail.com") == False



