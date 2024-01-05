from servicios.tokens.generate_tokens import get_access_token
from dotenv import load_dotenv
from os import environ
from servicios.tokens.read_token import TokenReader
import jwt


        

#NOTE: Integration test
def test_serv_can_read_jwt_token():
    load_dotenv()
    key = environ["AUTH_TOKEN_KEY"]
    token = get_access_token(minutes_time_delta=3,payload="hola")
    sut = TokenReader()
    sut_resp = sut.read(token=token,alg="HS256",key=key)
    assert sut_resp["sub"] == 'hola'
