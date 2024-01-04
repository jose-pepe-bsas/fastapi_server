from servicios.account.auth import Auth,token_reader,logged_users

"""
Auth module for boilerplate

Concern is validate that User Was Logged In
"""


def test_user_only_can_acess_if_access_token_has_his_id():
    sut_response = Auth().ask_access(user_token={'user_id':3},token_reader=token_reader(),logged_users=logged_users())
    assert sut_response
