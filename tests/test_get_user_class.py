from api.api_client_class import UserApi

def test_get_user_class():

    api = UserApi()

    response = api.get_user(1)

    assert response.status_code == 200