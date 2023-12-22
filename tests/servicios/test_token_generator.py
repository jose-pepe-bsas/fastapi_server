from servicios.tokens.generate_tokens import get_access_token
from datetime import datetime,timedelta,timezone
import jwt

KEY = "Testing123"
ALG = "HS256"

def read_token(token:str,key:str=KEY,alg=ALG):
    return jwt.decode(jwt= token,key=key,algorithms=alg)

def test_serv_should_return_access_token():
    """
    Generacion de token de acceso.

    Nota: Para el uso del componente el dato "payload" sera enviado como carga util
    """
    minutes_time_delta = 3 
    payload = {"user_email":"jose.s.contacto@gmail.com"}
    key = "crypt key"
    sut_response = get_access_token(minutes_time_delta=minutes_time_delta,
                                    payload=payload,
                                    key=key)

    assert type(sut_response) is str and len(sut_response)>0

def test_token_exp_time_should_be_setted():
    """
    Validacion de la expiracion del token 

    Dado que NO es responsabilidad del componente la validacion,
    aqui se asegura que la expiracion es asignada.

    Nota: El tiempo se envia al componente en minutos
    """
    actual_time_delta = 3
    sut_response = get_access_token(minutes_time_delta=actual_time_delta,
                                    payload="julian",
                                    key=KEY)
    token_exp= read_token(sut_response,KEY)["exp"] 
    assert type(token_exp) is int


