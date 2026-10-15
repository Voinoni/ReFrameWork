from api.base_api import BaseApi

def test_correlation_id():

    api = BaseApi()

    response = api.get(
        "/users/1"
    )

    print(response.headers)
