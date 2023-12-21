"""Componente de autenticacion para sesiones del sistema"""
class Login:

    def log_user_in(self,user_email:str=None,user_password:str=None,db=None) -> dict:
        if not None in [user_email,user_password]:
            if not db.exists(user_email):
                raise UserIsNotRegistered()

        credential = {
            'access_token':'sflkadskljfsdl',
            'refresh_token':'asdflsdkjlksdfj'
                          }
        return credential

class UserIsNotRegistered(BaseException):
    pass
