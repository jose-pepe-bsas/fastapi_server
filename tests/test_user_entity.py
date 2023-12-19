from entities.user import User

def test_user_should_exists_by_email_pass_roles():
    email = "jose.s.contacto@gmail.com"
    password = "Email123"
    roles = 3 
    sut = User(email=email,password=password,roles=roles) 
    assert sut is not None
    assert sut.email == email
    assert sut.password== password
    assert sut.roles == roles

