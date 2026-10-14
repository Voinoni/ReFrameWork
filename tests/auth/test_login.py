import requests


def test_login():

    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = requests.post(
        "https://dummyjson.com/auth/login",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    print(body["accessToken"])