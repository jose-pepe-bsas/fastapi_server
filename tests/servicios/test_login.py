from servicios.repo.user_repo import Repo 
from uuid import uuid4
import pytest
from tests.helpers.user_factory import UserFactory
from tests.helpers.stub_repo_factory import StubRepoFactory
from servicios.login import Login, UserIsNotRegistered
from dotenv import load_dotenv
import os

load_dotenv()
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
    sut_response = sut.log_user_in("jose.s.contacto@gmail.com","Password123",db=StubRepoFactory().get_factory(exists=True).with_id(id))
    assert sut.get_all_active_logged()[0]==id

    
def test_sut_should_validate_password_matching():
    actual_pass = "Password123!"
    wrong_pass = "AnotherPass321¡"
    email = "jose.s.contacto@gmail.com"
    user_id = uuid4()
    db = StubRepoFactory().get_factory(
        exists=True
    ).with_id(user_id).with_pass(actual_pass).with_email(email)

    sut_response = Login().validate_password(input=wrong_pass,email=email,db=db)
    assert sut_response is False
