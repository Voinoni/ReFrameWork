# tests/auth/test_auth_token_fixture.py

import requests


def test_auth_token_fixture(auth_token):

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.get(
        "https://dummyjson.com/auth/me",
        headers=headers
    )

    assert response.status_code == 200

    print("✅ Token works")
