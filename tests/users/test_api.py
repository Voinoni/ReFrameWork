from api.api_client_class import UserApi

def test_get_user():

    api = UserApi()

    response = api.get_user(2)

    assert response.status_code == 200