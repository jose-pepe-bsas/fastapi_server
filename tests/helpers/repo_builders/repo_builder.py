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

