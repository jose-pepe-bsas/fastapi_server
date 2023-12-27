from entities.authuser import AuthUser
from tests.helpers.user_builders.auth_user_builder import AuthUserBuilder

def test_builder_should_return_a_registered_user():
    """
    Instanciamiento de un objeto AuthUser siguiendo el esquema siguiente:
    
    class User(BaseModel):
        email:str
        password:str
    """
    sut = AuthUserBuilder().with_password("Pass123").build() 
    assert type(sut) is AuthUser
    assert sut.email is not None
    assert sut.password is "Pass123"
