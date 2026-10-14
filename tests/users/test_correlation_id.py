import requests


def test_correlation_id():

    response = requests.get(
        "https://dummyjson.com/users/1"
    )

    print(response.headers)
