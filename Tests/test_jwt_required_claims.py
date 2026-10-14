# tests/test_jwt_required_claims.py

import jwt
import requests

def test_jwt_required_claims():

    login_payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = requests.post(
        "https://dummyjson.com/auth/login",
        json=login_payload
    )

    token = response.json()["accessToken"]

    payload = jwt.decode(
        token,
        options={"verify_signature": False}
    )

    required_claims = [
        "id",
        "username",
        "email",
        "iat",
        "exp"
    ]

    for claim in required_claims:
        assert claim in payload