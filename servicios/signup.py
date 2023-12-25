from entities.user import User 
from entities.trySignUpUser import RegisterUser
import uuid
class SignUp:
    def create_user(self,user:RegisterUser=None,db:list=None):
        if not "@" in user.email:
            raise ValueError()
        for former_user in db.get_all():
            if former_user.email == user.email:
                raise ValueError()
        id = self._get_user_id()
        user_to_register = User(email=user.email,password=user.password,roles=0,id=id)
        db.save(user=user_to_register)


    def _get_user_id(self) -> str:
        return str(uuid.uuid4())
