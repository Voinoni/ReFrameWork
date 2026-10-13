import requests

def test_login_without_password():

    url = "https://dummyjson.com/auth/login"

    payload = {
        "email": "peter@klaven"
    }

    response = requests.post(url, json=payload)

    print(response.status_code)
    print(response.json())

    assert response.status_code == 400

    print("✅ Negative Test Passed")