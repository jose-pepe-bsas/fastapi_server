from entities.trySignUpUser import RegisterUser
from tests.helpers.sign_up_user_factory import SignUpUserFactory

def test_factory_should_return_standard_signup_user():
    """ 
    Instanciamiento de un objeto UserRegistered siguiendo el esquema siguiente:

    class RegisterUser(BaseModel):
        email:str
        password:str
    """
    sut = SignUpUserFactory.sign_up_user_factory
    assert type(sut.email) is str
    assert type(sut.password) is str
    
    
