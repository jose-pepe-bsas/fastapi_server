from entities.user import User 
from tests.helpers.user_factories.registered_user_factory import RegisteredUserFactory


def test_factory_should_return_a_standard_registered_user():
    """
    Instanciamiento de un objeto UserRegistered siguiendo el esquema siguiente:

    class User(BaseModel):
        email:str
        password:str
        roles:int 
        id:None | str
    """
    sut = RegisteredUserFactory.registered_user
    assert type(sut.email) is str
    assert type(sut.password) is str
    assert type(sut.roles) is int
    assert type(sut.id) == str

    
