class SignUp:
    def create_user(self,user:dict=None,db:list=None):
        if not "@" in user["email"]:
            raise ValueError()
        for former_user in db:
            if former_user["email"]==user["email"]:
                raise ValueError()
        db.append(user)
