from servicios.tokens.generate_tokens import get_access_token

def test_serv_should_return_access_token():
    """
    Generacion de token de acceso.

    Nota: Para el uso del componente el dato "payload" sera enviado como carga util
    """
    minutes_time_delta = 3 
    payload = {"user_email":"jose.s.contacto@gmail.com"}
    key = "crypt key"
    sut_response = get_access_token(minutes_time_delta=minutes_time_delta,
                                    payload=payload,
                                    key=key)

    assert type(sut_response) is str and len(sut_response)>0
