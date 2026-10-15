from api.base_api import BaseApi

def test_login_without_password():
    api = BaseApi()
    url = "/auth/login"

    payload = {
        "email": "peter@klaven"
    }

    response = api.post(url, payload)

    print(response.status_code)
    print(response.json())

    assert response.status_code == 400

    print("✅ Negative Test Passed")