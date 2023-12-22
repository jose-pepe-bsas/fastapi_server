import jwt
from datetime import datetime,timedelta,timezone

REFRESH_TIME_EXP = 60 * 3

def get_access_token(minutes_time_delta:int=None,payload:str=None,key:str=None,type:str="AUTH") -> str:
    exp =  datetime.now(tz=timezone.utc) + timedelta(minutes=minutes_time_delta)
    if type=="REFRESH":
        exp = datetime.now(tz=timezone.utc) + timedelta(minutes=REFRESH_TIME_EXP)
    to_encode_auth = {"exp": exp, "sub": payload}
    token = jwt.encode(to_encode_auth, key=key, algorithm="HS256")
    return token

