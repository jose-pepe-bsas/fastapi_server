from pydantic import BaseModel
from entities.authuser import AuthUser


class AuthUserFactory:
    auth_user_factory:AuthUser=AuthUser(
        email="jose.s.contacto@gmail.com",
        password="Password123"
    )
