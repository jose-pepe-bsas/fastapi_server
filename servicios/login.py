"""Componente de autenticacion para sesiones del sistema"""
class Login:

    def log_user_in(self,user_email:str=None,user_password:str=None) -> dict:
        if not None in [user_email,user_password]:
            credential = {
                'access_token':'sflkadskljfsdl',
                'refresh_token':'asdflsdkjlksdfj'
                          }
            return credential
