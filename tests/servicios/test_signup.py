from servicios.signup import SignUp
from tests.helpers.repo_builders.repo_builder import UserRepoBuilder
from tests.helpers.user_factories.sign_up_user_factory import SignUpUserFactory
from tests.helpers.user_builders.auth_user_builder import AuthUserBuilder
from uuid import UUID
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

user = SignUpUserFactory.sign_up_user_factory


@pytest.fixture(autouse=True,name="clean_db")
def clean_db():
    db._db = []
    yield
    db._db = []

#TODO: Cambiar el parametro user por el envio de los parametros de User, email y password
def test_serv_should_create_a_user_with_roles_email_pass():
    sut = SignUp()
    sut = SignUp().create_user(user=user, db=db)
    assert db._db[0].email==user.email
    
def test_user_must_use_arroba_in_email():
    user =  AuthUserBuilder().with_email("jose.s.contactogmail.com").build()
    with pytest.raises(ValueError):
        db = []
        sut = SignUp().create_user(user=user, db=db)

def test_user_must_not_exists_before_saving():
    repo = UserRepoBuilder().build()
    with pytest.raises(ValueError):
        sut = SignUp().create_user(user=user,db=repo)


def test_should_get_an_user_id():
    sut = SignUp().create_user(user=user 
                               ,db=db)
    id = db.get_all()[0].id
    assert type(id) is UUID and len(str(id)) > 0

