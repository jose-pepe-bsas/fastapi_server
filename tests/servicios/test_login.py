from servicios.repo.user_repo import Repo 
import pytest
from tests.helpers.user_factory import UserFactory
from tests.helpers.stub_repo_factory import StubRepoFactory
from servicios.login import Login, UserIsNotRegistered
"""Componente de autenticacion para sesiones del sistema"""



def test_should_obtain_access_and_refresh_token_by_registered_user():
    sut_response = Login().log_user_in("jose.s.contacto@gmail.com","Password123",db=StubRepoFactory().get_factory(exists=True))
    assert type(sut_response["access_token"]) is str and len(sut_response["access_token"])>0
    assert type(sut_response["refresh_token"]) is str and len(sut_response["refresh_token"])>0

def test_should_raise_user_doesnt_exists_exception_if_user_isnt_registered():
    with pytest.raises(UserIsNotRegistered):
        sut_response = Login().log_user_in("jose.s.contacto@gmail.com","Password123",db=StubRepoFactory().get_factory(exists=False))


def test_should_keep_memory_id():
    id = "cadenageneradaaut"
    sut = Login()
    sut.keep_id_in_memory(id)
    assert sut.get_all_active_logged()[0]==id



# validar user id 
# encriptar y desencript pass -> bycrpt(user_pass)
# desencript token -> jwt.decode(token,key)
#


#TODO: should_obtain_id_for_session_using_user_data():
#    sut = Login().log_user_in("jose.s.contacto@gmail.com","Password123")
#it gonna be gotten by hash user roles, email and password, using a secure hash key

#TODO: User should be restringed by his permissions
