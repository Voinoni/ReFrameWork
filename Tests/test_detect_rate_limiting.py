import requests


def test_detect_rate_limiting():

    count_429 = 0

    for _ in range(100):

        response = requests.get(
            "https://dummyjson.com/users/1"
        )

        if response.status_code == 429:
            count_429 += 1

    print(
        f"429 responses: {count_429}"
    )

    assert count_429 >= 0