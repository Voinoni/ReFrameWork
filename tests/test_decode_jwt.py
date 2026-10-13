import jwt
import requests


def test_decode_jwt():

    login_payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    login_response = requests.post(
        "https://dummyjson.com/auth/login",
        json=login_payload
    )

    assert login_response.status_code == 200

    token = login_response.json()["accessToken"]

    payload = jwt.decode(
        token,
        options={"verify_signature": False}
    )

    print("\nJWT Payload:")
    print(payload)

    assert payload is not None
    assert payload["username"] == "emilys"
    assert payload["email"].endswith("@x.dummyjson.com")
    assert payload["exp"] > payload["iat"]
    #assert payload["role"] == "admin"