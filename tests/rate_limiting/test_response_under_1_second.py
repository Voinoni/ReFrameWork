import requests


def test_response_under_1_second():

    response = requests.get(
        "https://dummyjson.com/users/1"
    )

    response_time = response.elapsed.total_seconds()

    print(f"\nResponse time: {response_time}")

    assert response_time < 1