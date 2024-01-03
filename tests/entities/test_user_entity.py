from entities.user import RegisteredUser

def test_registered_user_should_exists_by_email_pass_roles():
    email = "jose.s.contacto@gmail.com"
    password = "Email123"
    roles = 3 
    sut = RegisteredUser(email=email,password=password,roles=roles,id=None) 
    assert sut is not None
    assert sut.email == email
    assert sut.password== password
    assert sut.roles == roles

