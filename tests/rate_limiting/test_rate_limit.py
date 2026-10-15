from api.base_api import BaseApi


def test_multiple_requests():

    successful_requests = 0

    api = BaseApi()

    for _ in range(20):

        response = api.get(
            "/users/1"
        )

        if response.status_code == 200:
            successful_requests += 1

    assert successful_requests == 20

    print(f"Successful Requests: {successful_requests}")