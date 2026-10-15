from api.base_api import BaseApi
import time


def test_response_time_under_load():
    api = BaseApi()
    times = []

    for _ in range(20):

        start = time.time()

        response = api.get(
            "/users/1"
        )

        end = time.time()

        times.append(
            end - start
        )

        assert response.status_code == 200

    average = sum(times) / len(times)

    print(
        f"Average Response Time: {average}"
    )

    assert average < 2