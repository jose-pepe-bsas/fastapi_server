from servicios.account.auth import Auth
from servicios.tokens.generate_tokens import get_access_token
from servicios.tokens.read_token import TokenReader

"""
Auth module for boilerplate

Concern is validate that User Was Logged In
"""

class TokenValidatorStub:
    def is_token_valid(self,token):
        return True

class logged_usersStub:
    def is_user(self,user_id=None):
        return True
#NOTE: Fix string indices must be integers error
#NOTE: Use stub token reader to isolate test
#def test_user_only_can_acess_if_access_token_has_his_id():
#    token = get_access_token(minutes_time_delta=3,payload="hola")
#    sut_response = Auth().ask_access(user_token=token,
#                                     token_validator=TokenValidatorStub(),
#                                     logged_users=logged_usersStub(),
#                                     token_reader=TokenReader())
#    assert sut_response
