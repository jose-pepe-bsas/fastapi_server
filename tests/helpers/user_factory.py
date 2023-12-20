from entities.user import User
class UserFactory:
    def create_user(self,email="pedroRomero@gmail.com",password="Secreta123!",roles=0):
        return User(email=email,password=password,roles=roles)
