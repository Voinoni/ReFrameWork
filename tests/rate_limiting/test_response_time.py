from api.base_api import BaseApi


def test_response_time_under_2_seconds():
    api = BaseApi()

    response = api.get("/users/1")

    assert response.status_code == 200

    response_time = response.elapsed.total_seconds()

    print(f"\nResponse Time: {response_time:.3f} sec")

    assert response_time < 2, (
        f"Response time {response_time:.3f}s exceeded 2 seconds"
    )