from entities.user import RegisteredUser
from entities.trySignUpUser import SignUpUser 
import uuid
class SignUp:
    def create_user(self,user:SignUpUser=None,db:list=None):
        if not "@" in user.email:
            raise ValueError()
        if db.exists(user.email):
                raise ValueError()
        id = self._get_user_id()
        user_to_register = RegisteredUser(email=user.email,password=user.password,roles=0,id=id)
        db.save(user=user_to_register)


    def _get_user_id(self) -> str:
        return str(uuid.uuid4())
