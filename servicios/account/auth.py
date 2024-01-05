from servicios.tokens.read_token import TokenReader
from os import environ
from dotenv import load_dotenv

    
class Auth:
    def ask_access(self,user_token=None,token_reader=None,token_validator=None,logged_users=None):
        load_dotenv()
        key = environ["AUTH_TOKEN_KEY"]
        if not token_validator.is_token_valid(user_token):
            raise ValueError()
        user_id = token_reader.read(user_token,key=key)['sub']
        if logged_users.is_user(user_id=user_id):
            return True
