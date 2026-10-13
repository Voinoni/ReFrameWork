import requests

def test_invalid_token():

    headers = {
        "Authorization": "Bearer dummy-token"
    }

    response = requests.get(
        "https://dummyjson.com/auth/me",
        headers=headers
    )

    assert response.status_code == 401