from servicios.repo.user_repo import Repo
from tests.helpers.user_factories.registered_user_factory import RegisteredUserFactory
from tests.helpers.user_builders.registered_user_builder import RegisteredUserBuilder
"""Modulo de repo de usuarios"""

user = RegisteredUserFactory.registered_user

def test_serv_should_know_if_a_user_exists_or_not():
    sut = Repo(db=[])
    sut.save(user) 
    assert sut.exists(user_email=user.email)
    assert sut.exists(user_email="manolo@gmail.com") == False


def test_repo_should_return_all_users():
    sut = Repo(db=[])
    user1= RegisteredUserBuilder(email="julian@gmail.com").build()
    user2= RegisteredUserBuilder(email="jose.s.contacto@gmail.com").build()
    sut.save(user1)
    sut.save(user2)
    resp = sut.get_all()
    assert resp[0].email == "julian@gmail.com"
    assert resp[1].email == user.email



def test_repo_should_get_id_from_email():
    sut = Repo(db=[])
    id = user.id
    sut.save(user) 
    sut_response = sut.get_id_by_email(user.email)
    assert sut_response == id
