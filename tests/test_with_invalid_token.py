import requests

def test_with_invalid_token():

    headers = {
        "Authorization": "Bearer invalid-token"
    }

    response = requests.get(
        "https://dummyjson.com/auth/me",
        headers=headers
    )

    assert response.status_code == 401