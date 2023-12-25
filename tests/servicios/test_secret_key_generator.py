from servicios.envkeysgen import generate_env_key,read_env_key

def test_secret_key_should_set_an_env_key():   
    generate_env_key("test_key")
    sut_respose = read_env_key("test_key")
    assert sut_respose is not None
    assert type(sut_respose) is str

