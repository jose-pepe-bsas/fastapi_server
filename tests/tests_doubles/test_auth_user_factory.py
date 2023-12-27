from entities.authuser import AuthUser
from tests.helpers.auth_user_factory import AuthUserFactory


def test_factory_should_return_a_standard_auth_user():
    """
    Instanciamiento de un objeto AuthUser siguiendo el esquema siguiente:

    class AuthUser(BaseModel):
        email:str
        password:str
    """
    sut = AuthUserFactory.auth_user_factory
    assert type(sut.email) is str
    assert type(sut.password) is str

    
