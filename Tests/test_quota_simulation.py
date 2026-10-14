import requests


def test_quota_simulation():
    successful = 0

    for _ in range(50):
        response = requests.get("https://dummyjson.com/users/1")

        if response.status_code == 200:
            successful += 1

    print(f"Successful Requests: {successful}")

    assert successful > 0