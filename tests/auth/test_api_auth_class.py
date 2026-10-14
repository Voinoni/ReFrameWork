from api.api_auth_class import AuthApi


def test_auth_login():

    auth = AuthApi()

    response = auth.login(
        "emilys",
        "emilyspass"
    )

    assert response.status_code == 200

    print("✅ Test test_auth_login_class Passed")

#--------------Test---------------Search User API
from api.api_client_class import UserApi


def test_search_user():

    api = UserApi()

    response = api.search_user("Emily")

    assert response.status_code == 200

    body = response.json()

    assert len(body["users"]) > 0

    print(body["users"], "✅ user found")