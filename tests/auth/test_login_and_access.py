import requests

def test_login_and_access():

    token = "dummy-token"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://dummyjson.com/auth/me",
        headers=headers
    )

    assert response.status_code == 401