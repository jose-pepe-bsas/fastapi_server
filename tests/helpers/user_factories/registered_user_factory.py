from entities.user import User
from uuid import UUID,uuid4

class RegisteredUserFactory:
    registered_user:User = User(email="jose.s.contacto@gmail.com",
                    password= "blablabla123",
                    roles=3,
                    id=uuid4())
