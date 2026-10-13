import pytest
import requests

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_users(user_id):

    response = requests.get(
        f"https://dummyjson.com/users/{user_id}"
    )

    assert response.status_code == 200