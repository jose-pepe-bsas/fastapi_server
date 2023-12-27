from servicios.envkeysgen import generate_env_key_value,read_env_key,set_key
import pytest
import os

@pytest.fixture(autouse=True)
def clean_env():
    if os.path.isfile(".env"):
        os.remove(".env")
        os.system("touch .env")
    os.system("touch .env")
    yield
    if os.path.isfile(".env"):
        os.remove(".env")

#NOTE: Integration test
def test_secret_key_can_be_read():
    key_setted = "ImaKey"
    key_name = "Keyid"
    os.system("python -m dotenv set "+key_name+" "+key_setted)
    sut_response = read_env_key(key_name=key_name)
    assert sut_response == key_setted

def test_secret_key_value_can_be_generated():
    sut_response = generate_env_key_value()
    assert type(sut_response) is str and len(sut_response) > 0

#NOTE: Integration
def test_generator_should_save_keys_in_a_dot_env_file():
    generated_key_value = generate_env_key_value()
    key_name ="testing_key"
    set_key(key_name,generated_key_value)
    readed = str()
    with open(".env") as dot_env_file:
        lines = dot_env_file.readlines()
        for line in lines:
            print(line)
            if line.startswith(key_name):
                readed = line.removeprefix(key_name+"=")
    assert readed == generated_key_value
    assert read_env_key(key_name)
