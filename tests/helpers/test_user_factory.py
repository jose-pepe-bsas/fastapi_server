from tests.helpers.user_factory import UserFactory

def test_factory_should_create_a_standard_user():
    assert UserFactory().create_user(email="jose.s.contacto@gmail.com",password="hola123",roles=2)["email"] == "jose.s.contacto@gmail.com"

