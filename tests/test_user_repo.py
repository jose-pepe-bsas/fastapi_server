from servicios.repo.user_repo import Repo
"""Modulo de repo de usuarios"""


def test_serv_should_know_if_a_user_exists_or_not():
    sut = Repo(db=[])
    sut.save(user={"email":"jose.s.contacto@gmail.com"})
    assert sut.exists(user_email="jose.s.contacto@gmail.com")
    assert sut.exists(user_email="manolo@gmail.com") == False



