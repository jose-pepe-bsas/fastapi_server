from tests.helpers.user_builders.try_sign_up_user_builder import TrySignUpUserBuilder
from entities.trySignUpUser import SignUpUser 

def test_builder_should_return_a_try_sign_up_user():
    """
    Instanciamiento de un objeto RegisterUser siguiendo el esquema siguiente:
    
    class SignUpUser(BaseModel):
        email:str
        password:str
    """
    sut = TrySignUpUserBuilder().with_password("Pass123").build() 
    assert type(sut) is SignUpUser  
    assert sut.email is not None
    assert sut.password == "Pass123"
