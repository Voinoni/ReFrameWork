from api.base_api import BaseApi


def test_quota_simulation():
    successful = 0
    api = BaseApi()

    for _ in range(50):
        response = api.get("/users/1")

        if response.status_code == 200:
            successful += 1

    print(f"Successful Requests: {successful}")

    assert successful > 0