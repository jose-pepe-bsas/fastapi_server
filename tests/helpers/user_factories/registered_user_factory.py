from entities.user import RegisteredUser 
from uuid import UUID,uuid4

class RegisteredUserFactory:
    registered_user:RegisteredUser= RegisteredUser(email="jose.s.contacto@gmail.com",
                    password= "blablabla123",
                    roles=3,
                    id=str(uuid4()))
