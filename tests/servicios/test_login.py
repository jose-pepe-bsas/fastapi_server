from servicios.repo.user_repo import Repo 
from uuid import uuid4
import pytest
from tests.helpers.user_factory import UserFactory
from tests.helpers.user_factories.auth_user_factory import AuthUserFactory
from tests.helpers.stub_repo_factory import StubRepoFactory
from servicios.login import Login, UserIsNotRegistered
from tests.helpers.user_factories.registered_user_factory import RegisteredUserFactory
from dotenv import load_dotenv
import os

load_dotenv()
"""Componente de autenticacion para sesiones del sistema"""


user = AuthUserFactory.auth_user_factory

def test_should_obtain_access_and_refresh_token_by_registered_user():
    sut_response = Login().log_user_in(user.email,
                                       user.password,
                                       db=StubRepoFactory().get_factory(exists=True))

    assert type(sut_response["access_token"]) is str and len(sut_response["access_token"])>0
    assert type(sut_response["refresh_token"]) is str and len(sut_response["refresh_token"])>0

def test_should_raise_user_doesnt_exists_exception_if_user_isnt_registered():
    with pytest.raises(UserIsNotRegistered):

        sut_response = Login().log_user_in(user.email,
                                           user.password,
                                           db=StubRepoFactory().get_factory(exists=False))


def test_should_keep_memory_id():
    id = "Random ID"
    sut = Login()
    sut_response = sut.log_user_in(user.email,
                                   user.password,
                                   db=StubRepoFactory().get_factory(exists=True).with_id(id))

    assert sut.get_all_active_logged()[0]==id

    
def test_sut_should_validate_password_matching():
    user = RegisteredUserFactory.registered_user
    wrong_pass = "AnotherPass321¡"
    db = StubRepoFactory().get_factory(
        exists=True
    ).with_id(user.id).with_pass(user.password).with_email(user.email)

    sut_response = Login().validate_password(input=wrong_pass,
                                             email=user.email,db=db)
    assert sut_response is False
