from api.base_api import BaseApi


def test_response_under_1_second():
    api = BaseApi()

    response = api.get(
        "/users/1"
    )

    response_time = response.elapsed.total_seconds()

    print(f"\nResponse time: {response_time}")

    assert response_time < 1