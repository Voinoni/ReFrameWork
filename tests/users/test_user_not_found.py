import requests


def test_user_not_found():

    response = requests.get(
        "https://dummyjson.com/users/999999"
    )
    print(response.status_code)
    print(response.text)
    assert response.status_code == 404
