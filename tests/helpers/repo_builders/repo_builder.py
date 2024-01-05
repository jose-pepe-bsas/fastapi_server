from tests.helpers.stub_user_repo import StubRepo
from servicios.protocols.entityrepo import ENTITY_REPO
from entities.user import RegisteredUser
class UserRepoBuilder:

    def __init__(self):
        self._exists = True
        self._db = []
        self._id_by_email = "IdGenerated"
        self._user = RegisteredUser(email="jose.s.contacto@gmail.com",
                                    password = "Password123",
                                    id = "GeneratedId",
                                    roles = 1
                                    )

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

    def build(self) -> ENTITY_REPO:
        repo = StubRepo(exists=self._exists)
        repo._db = self._db
        repo._exists = self._exists
        repo._user = self._user
        repo._id = self._id_by_email
        return repo

