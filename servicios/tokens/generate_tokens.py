import jwt
from datetime import datetime,timedelta,timezone

def get_access_token(minutes_time_delta:int=None,payload:str=None,key:str=None) -> str:
    exp =  datetime.now(tz=timezone.utc) + timedelta(minutes=minutes_time_delta)
    to_encode_auth = {"exp": exp, "sub": payload}
    token = jwt.encode(to_encode_auth, key=key, algorithm="HS256")
    return token

