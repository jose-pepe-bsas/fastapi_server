from entities.user import RegisteredUser
from servicios.protocols.builders import BUILDER
from servicios.entitycreators.registered_user_builder import RegisteredUserBuilder
from entities.trySignUpUser import SignUpUser 
import uuid

class SignUp():
    def create_user(self,user:SignUpUser=None,db:list=None,user_builder:BUILDER=RegisteredUserBuilder()):
        id = self._get_user_id()
        to_build = user_builder.with_email(email=user.email).with_password(password=user.password).with_roles(roles=0).with_id(id=id)

        if db.exists(user.email):
            raise AlreadySignedUser()

        if to_build.is_valid():
            db.save(to_build.build())
        else:
            raise NotValidSignUpException()


    def _get_user_id(self) -> str:
        return str(uuid.uuid4())

class NotValidSignUpException(BaseException):
    pass

class AlreadySignedUser(BaseException):
    pass
