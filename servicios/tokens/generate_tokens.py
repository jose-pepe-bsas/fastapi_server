import jwt

def get_access_token(minutes_time_delta:int=None,payload:str=None,key:str=None) -> str:
    to_encode_auth = {"exp": minutes_time_delta, "sub": payload}
    token = jwt.encode(to_encode_auth, key=key, algorithm="HS256")
    return token

