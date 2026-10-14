import requests


def test_multiple_requests():

    successful_requests = 0

    for _ in range(20):

        response = requests.get(
            "https://dummyjson.com/users/1"
        )

        if response.status_code == 200:
            successful_requests += 1

    assert successful_requests == 20