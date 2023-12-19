from entities.user import User

def test_user_should_exists_by_email_pass_roles():
    email = "jose.s.contacto@gmail.com"
    password = "Email123"
    roles = 3 
    assert User(email,password,roles) is not None

