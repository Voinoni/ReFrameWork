from api.base_api import BaseApi

def test_user_not_found():

    api = BaseApi()

    response = api.delete(
        "/users/999999"
    )
    print(response.status_code)
    print(response.text)
    assert response.status_code == 404
