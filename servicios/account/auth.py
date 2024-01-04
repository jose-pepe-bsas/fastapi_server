class token_reader:
    def is_token_valid(self,token:str):
        return True

    def read(self,token:dict=None):
        return {'id':3}

class logged_users:
    def is_user(self,user_id=None):
        return True
    
class Auth:
    def ask_access(self,user_token=None,token_reader=None,logged_users=None):
        if not token_reader.is_token_valid(user_token):
            raise ValueError()
        user_id = token_reader.read(user_token)['id']
        if logged_users.is_user(user_id=user_id):
            return True
