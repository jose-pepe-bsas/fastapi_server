from servicios.repo.user_repo import Repo
from uuid import uuid4
from tests.helpers.stub_repo_factory import StubRepo

class UserRepoBuilder:

    def __init__(self):
        self._exists = True
        self._db = []
        self._id_by_email = 40
        self._user = {
            'email':"jose.s.contacto@gmail.com",
            'password':'Password123'
        } 

    def with_this_db(self,db):
        self._db = db
        return self

    def with_id_by_email(self,id):
        self._id_by_email=id 
        return self

    def with_exists(self,exists):
        self._exists= exists
        return self

    def with_user(self,user):
        self._user = user
        return self

    def build(self):
        repo = StubRepo(exists=self._exists)
        repo._db = self._db
        repo._exists = self._exists
        repo._user = self._user
        repo._id = self._id_by_email
        return repo

def test_repo_builder_should_generate_custom_repo():
    db = []
    exists = False
    id_by_email = uuid4()
    passw = "Pass123"
    user = {"user_value":"value"}
    sut = UserRepoBuilder().with_this_db(
        db
    ).with_exists(
        exists
    ).with_id_by_email(
        id_by_email
    ).with_user(
        user
    ).build()

    assert db == sut._db
    assert sut.exists("stub@gmail.com") is False
    assert sut.get_id_by_email("stub@gmail.com") == id_by_email
    assert sut.get_user_by_id(143)["user_value"] == "value"
                                                
