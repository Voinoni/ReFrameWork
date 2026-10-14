import requests


def test_retry_after_header():

    response = requests.get(
        "https://dummyjson.com/users/1"
    )

    if response.status_code == 429:
        assert "Retry-After" in response.headers