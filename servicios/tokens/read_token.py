import jwt
class TokenReader:
    def read(self,token:dict=None,alg:str="HS256",key:str=None):
        return jwt.decode(jwt= token,key=key,algorithms=alg)
