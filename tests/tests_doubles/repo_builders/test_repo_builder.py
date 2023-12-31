from tests.helpers.repo_builders.repo_builder import UserRepoBuilder

def test_repo_builder_should_generate_custom_repo():
    db = []
    exists = False
    id_by_email = "IdGenerated"
    passw = "Pass123"
    user = {"user_value":"value"}
    sut = UserRepoBuilder().with_this_db(
        db
    ).with_exists(
        exists
    ).with_id_by_email(
        id_by_email
    ).with_user(
        user
    ).build()

    assert db == sut._db
    assert sut.exists("stub@gmail.com") is False
    assert sut.get_id_by_email("stub@gmail.com") == id_by_email
    assert sut.get_user_by_id(143)["user_value"] == "value"
                                                
