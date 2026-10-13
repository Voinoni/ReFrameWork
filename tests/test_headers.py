import requests


def test_headers():

    response = requests.get(
        "https://reqres.in/api/users/2"
    )

    assert "application/json" in response.headers[
        "Content-Type"
    ]