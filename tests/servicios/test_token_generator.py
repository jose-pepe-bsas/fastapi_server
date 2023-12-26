from servicios.tokens.generate_tokens import get_access_token
from dotenv import load_dotenv
from datetime import datetime,timedelta,timezone
from servicios.envkeysgen import generate_env_key_value,set_key
import jwt
from os import environ

KEY = generate_env_key_value()
ALG = "HS256"

set_key("AUTH_TOKEN_KEY", KEY)

def read_token(token:str,key:str=KEY,alg=ALG):
    load_dotenv()
    key = environ["AUTH_TOKEN_KEY"]
    return jwt.decode(jwt= token,key=key,algorithms=alg)

def test_serv_should_return_access_token():
    """
    Generacion de token de acceso.

    Nota: Para el uso del componente el dato "payload" sera enviado como carga util
    """
    minutes_time_delta = 3 
    payload = {"user_email":"jose.s.contacto@gmail.com"}
    sut_response = get_access_token(minutes_time_delta=minutes_time_delta,
                                    payload=payload)

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
                                    payload="julian")
    token_exp= read_token(sut_response,KEY)["exp"] 
    assert type(token_exp) is int

def test_serv_should_return_an_refresh_token():
    refresh_token = get_access_token(minutes_time_delta=3,
                                     payload="hola",
                                     type="REFRESH")
    assert type(refresh_token) is str and len(refresh_token) >0
