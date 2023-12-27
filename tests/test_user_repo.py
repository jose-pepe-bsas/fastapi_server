from servicios.repo.user_repo import Repo
from tests.helpers.user_factory import UserFactory
from tests.helpers.user_factories.registered_user_factory import RegisteredUserFactory
import uuid
"""Modulo de repo de usuarios"""

user = RegisteredUserFactory.registered_user

def test_serv_should_know_if_a_user_exists_or_not():
    sut = Repo(db=[])
    sut.save(user) 
    assert sut.exists(user_email=user.email)
    assert sut.exists(user_email="manolo@gmail.com") == False


def test_repo_should_return_all_users():
    sut = Repo(db=[])
    sut.save(user)
    sut.save(UserFactory().create_user(email="julian@gmail.com"))
    resp = sut.get_all()
    assert resp[0].email == user.email
    assert resp[1].email == "julian@gmail.com"



def test_repo_should_get_id_from_email():
    sut = Repo(db=[])
    id = user.id
    sut.save(user) 
    sut_response = sut.get_id_by_email(user.email)
    assert sut_response == id
