"""
Modulo de creacion de cuenta de usuario

  . Crear servicio para generar un usuario en base a roles y datos (correo, passwords, etc)
  . Exponer un endpoint para generar usuario
  . Crear servicio de persistencia
  . Crear y lanzar excepciones en casos limites
    El usuario no puede existir
    El email debe ser valido teniendo un '@'

"""

class SignUp:
    def create_user(self,user:dict=None,db:list=None):
        db.append(user)

def test_serv_should_create_a_user_with_roles_email_pass():
    db = []
    sut = SignUp().create_user(user={
        "email":"jose.s.contacto@gmail.com",
        "password":"chocolateLoco2",
        "roles":1
    }, db=db)
    assert db[0]["email"]=="jose.s.contacto@gmail.com"
