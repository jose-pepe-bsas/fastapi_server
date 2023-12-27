from entities.authuser import AuthUser

class AuthUserBuilder:
    def __init__(self):
        self._email = "jose.s.contacto@gmail.com"
        self._password = "Password123"

    def with_email(self,email:str):
        self._email = email
        return self

    def with_password(self,password:str):
        self._password = password
        return self

    def build(self) -> AuthUser:
        return AuthUser(email=self._email,
                        password=self._password)

