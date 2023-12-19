class SignUp:
    def create_user(self,user:dict=None,db:list=None):
        if not "@" in user["email"]:
            raise ValueError()
        db.append(user)
