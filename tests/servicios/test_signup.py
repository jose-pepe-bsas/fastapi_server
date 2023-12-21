from servicios.signup import SignUp
from tests.helpers.user_factory import UserFactory
import pytest
from api.routes.users import db
"""
Modulo de creacion de cuenta de usuario

  . Crear servicio para generar un usuario en base a roles y datos (correo, passwords, etc)
  . Exponer un endpoint para generar usuario
  . Crear servicio de persistencia
  . Crear y lanzar excepciones en casos limites
    El usuario no puede existir
    El email debe ser valido teniendo un '@'

"""


@pytest.fixture(autouse=True,name="clean_db")
def clean_db():
    db._db = []
    yield
    db._db = []

def test_serv_should_create_a_user_with_roles_email_pass():
    sut = SignUp().create_user(user=UserFactory().create_user("jose.s.contacto@gmail.com"), db=db)
    assert db._db[0].email=="jose.s.contacto@gmail.com"
    
def test_user_must_use_arroba_in_email():
    with pytest.raises(ValueError):
        db = []
        sut = SignUp().create_user(user=UserFactory().create_user(email="jose.s.contactogmail.com"), db=db)

def test_user_must_not_exists_before_saving():
    with pytest.raises(ValueError):
        db = []
        sut = SignUp().create_user(user=UserFactory().create_user(email="jose.s.contactogmail.com"), db=db)
        sut = SignUp().create_user(user=UserFactory().create_user(email="jose.s.contactogmail.com"), db=db)


def test_should_get_an_user_id():
    sut_response = SignUp().get_user_id()
    assert type(sut_response) is str and len(sut_response) > 0

