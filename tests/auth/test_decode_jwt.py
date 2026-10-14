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

    #-----------Validate Mandatory Claims----------
    required_claims = [
    "username",
    "email",
    "iat",
    "exp"
    ]

    for claim in required_claims:
        assert claim in payload
    #-----------------------------------------------

        assert payload is not None
        assert payload["username"] == "emilys"
        assert payload["firstName"] == "Emily"
        assert payload["lastName"] == "Johnson"
        assert payload["email"].endswith("@x.dummyjson.com")
        assert payload["exp"] > payload["iat"]
        #assert payload["role"] == "admin"
        assert "email" in payload
        assert "iat" in payload
        assert "exp" in payload

#--------------Validate Invalid Login----------

from api.api_auth import login

def test_invalid_login():

    response = login(
        "fakeuser",
        "fakepassword"
    )

    assert response.status_code in [400, 401]
#---------------------------------------------
