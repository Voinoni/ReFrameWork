import requests


def test_bearer_token_header():

    headers = {
        "Authorization": "Bearer fake_jwt_token"
    }

    response = requests.get(
        "https://reqres.in/api/users/2",
        headers=headers
    )

    assert response.status_code == 401