import requests


def test_user_e2e():

    # Step 1 - Login
    login_payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    login_response = requests.post(
        "https://dummyjson.com/auth/login",
        json=login_payload
    )

    assert login_response.status_code == 200

    login_body = login_response.json()

    token = login_body["accessToken"]

    print("\nToken received successfully")

    # Step 2 - Access protected endpoint
    headers = {
        "Authorization": f"Bearer {token}"
    }

    user_response = requests.get(
        "https://dummyjson.com/auth/me",
        headers=headers
    )

    assert user_response.status_code == 200

    user_body = user_response.json()

    print("User:", user_body["firstName"])

    # Step 3 - Validate user data
    assert user_body["firstName"] == "Emily"
    assert user_body["email"] == "emily.johnson@x.dummyjson.com"
    assert user_body["address"]["city"] == "Phoenix"
    assert user_body["address"]["country"] == "United States"

    print(user_response.json())
    print("✅ End-to-End Test Passed")