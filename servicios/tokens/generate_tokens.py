import jwt
from datetime import datetime,timedelta,timezone
from os import environ,path
from dotenv import load_dotenv
from servicios.envkeysgen import generate_env_key_value,set_key


REFRESH_TIME_EXP = 60 * 3



def get_access_token(minutes_time_delta:int=None,payload:str=None,type:str="AUTH") -> str:
    load_dotenv()
    key = environ["AUTH_TOKEN_KEY"]
    exp =  datetime.now(tz=timezone.utc) + timedelta(minutes=minutes_time_delta)
    if type=="REFRESH":
        exp = datetime.now(tz=timezone.utc) + timedelta(minutes=REFRESH_TIME_EXP)
    to_encode_auth = {"exp": exp, "sub": payload}
    token = jwt.encode(to_encode_auth, key=key, algorithm="HS256")
    return token

