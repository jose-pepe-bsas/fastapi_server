from repo.user_repo import Repo 
from uuid import uuid4
import pytest
from tests.helpers.user_factories.auth_user_factory import AuthUserFactory
from servicios.account.login import Login, UserIsNotRegistered
from tests.helpers.user_factories.registered_user_factory import RegisteredUserFactory
from tests.helpers.repo_builders.repo_builder import UserRepoBuilder
from dotenv import load_dotenv
import os

load_dotenv()
"""Componente de autenticacion para sesiones del sistema"""


user = AuthUserFactory.auth_user_factory

def test_should_obtain_access_and_refresh_token_by_registered_user():
    repo = UserRepoBuilder().with_exists(True).build()
    sut_response = Login().log_user_in(user.email,
                                       user.password,
                                       db=repo)

    assert type(sut_response["access_token"]) is str and len(sut_response["access_token"])>0
    assert type(sut_response["refresh_token"]) is str and len(sut_response["refresh_token"])>0

def test_should_raise_user_doesnt_exists_exception_if_user_isnt_registered():
    with pytest.raises(UserIsNotRegistered):
        repo = UserRepoBuilder().with_exists(False).build()

        sut_response = Login().log_user_in(user.email,
                                           user.password,
                                           repo)


def test_should_keep_memory_id():
    id = "Random ID"
    repo = UserRepoBuilder().with_id_by_email(id).build()
    sut = Login()
    sut_response = sut.log_user_in(user.email,
                                   user.password,
                                   db=repo)

    assert sut.get_all_active_logged()[0]==id

    
def test_sut_should_validate_password_matching():
    user = RegisteredUserFactory.registered_user
    wrong_pass = "AnotherPass321¡"
    repo = UserRepoBuilder().with_exists(True).with_id_by_email(user.id).with_user(user).build()

    sut_response = Login().validate_password(input=wrong_pass,
                                             email=user.email,db=repo)
    assert sut_response is False
