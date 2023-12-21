import uuid
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

        acc_tok,refr_tok = self.get_auth_tokens()

        credential = {
            'access_token':acc_tok,
            'refresh_token':refr_tok
                          }
        return credential


    def get_auth_tokens(self,time_delta_auth:int=5,time_delta_refresh:int=10,payload_auth=None,payload_refresh=None,key="test123"):
        to_encode_auth = {"exp": time_delta_auth, "sub": payload_auth}
        auth_token = jwt.encode(to_encode_auth, key=key, algorithm="HS256")
        to_encode_refresh = {"exp": time_delta_refresh, "sub": payload_refresh}
        refresh_token = jwt.encode(to_encode_refresh, key=key, algorithm="HS256")
        return auth_token,refresh_token

    def keep_id_in_memory(self,id:str=None):
        if id is None:
            raise ValueError()
        self._active_logged.append(id)

    def get_all_active_logged(self):
        return self._active_logged



class UserIsNotRegistered(BaseException):
    pass
