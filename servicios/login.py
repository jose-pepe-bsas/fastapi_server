from servicios.tokens.generate_tokens import get_access_token
from servicios.envkeysgen import generate_env_key_value,set_key
import jwt
"""Componente de autenticacion para sesiones del sistema"""
class Login:

    def __init__(self):
        self._active_logged = list()

    def log_user_in(self,user_email:str=None,user_password:str=None,db=None) -> dict:
        if None in [user_email,user_password]:
            raise ValueError("Email and/or pass was none")
        
        if not db.exists(user_email):
            raise UserIsNotRegistered()

        acc_tok,refr_tok = self._get_auth_tokens()

        credential = {
            'access_token':acc_tok,
            'refresh_token':refr_tok
                          }

        user_id =db.get_id_by_email(user_email) 
        self._keep_id_in_memory(user_id)
        return credential


    def _get_auth_tokens(self,time_delta_auth:int=5,time_delta_refresh:int=10,payload_auth=None,payload_refresh=None,key="test123"):
        set_key("AUTH_TOKEN_KEY", generate_env_key_value())
        auth_token = get_access_token(minutes_time_delta = time_delta_auth,payload= payload_auth)
        refresh_token = get_access_token(minutes_time_delta = time_delta_auth,payload= payload_auth,type="REFRESH")
        return auth_token,refresh_token

    def _keep_id_in_memory(self,id:str=None):
        if id is None:
            raise ValueError()
        self._active_logged.append(id)

    def get_all_active_logged(self):
        return self._active_logged

    def validate_password(self,input=None,email=None,db=None):
        if not db.exists(email):
            raise UserIsNotRegistered()
        user_id = db.get_id_by_email(email)
        return db.get_user_by_id(user_id).password == input
    




class UserIsNotRegistered(BaseException):
    pass
