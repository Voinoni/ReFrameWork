import requests

BASE_URL = "https://dummyjson.com"

def test_invalid_login():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "username": "wrong",
            "password": "wrong"
        }
    )

    assert response.status_code == 400
    assert "Invalid credentials" in response.text

    print(response.status_code)
    print(response.text)