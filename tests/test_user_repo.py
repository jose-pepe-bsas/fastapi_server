from servicios.repo.user_repo import Repo
from tests.helpers.user_factory import UserFactory
"""Modulo de repo de usuarios"""


def test_serv_should_know_if_a_user_exists_or_not():
    sut = Repo(db=[])
    sut.save(UserFactory().create_user(email="jose.s.contacto@gmail.com"))
    assert sut.exists(user_email="jose.s.contacto@gmail.com")
    assert sut.exists(user_email="manolo@gmail.com") == False

#TODO: repo tiene que tener un metodo get all
#TODO: Para probar persistencia usando api, usar el metodo get user/user_id

def test_repo_should_return_all_users():
    sut = Repo(db=[])
    sut.save(UserFactory().create_user(email="jose.s.contacto@gmail.com"))
    sut.save(UserFactory().create_user(email="julian@gmail.com"))
    resp = sut.get_all()
    assert resp[0].email == "jose.s.contacto@gmail.com"
    assert resp[1].email == "julian@gmail.com"






