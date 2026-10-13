import pytest
import requests


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_users(user_id):

    response = requests.get(
        f"https://dummyjson.com/users/{user_id}"
    )

    assert response.status_code == 200, (
    f"Expected 200 but got {response.status_code}"
)

    body = response.json()

    assert body["id"] == user_id