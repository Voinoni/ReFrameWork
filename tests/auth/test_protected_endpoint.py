import requests


def test_protected_endpoint():

    response = requests.get(
        "https://dummyjson.com/users/1"
    )

    assert response.status_code == 200