import pytest
from api.base_api import BaseApi


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_users(user_id):
    api = BaseApi()

    response = api.get(
        f"/users/{user_id}"
    )

    assert response.status_code == 200, (
    f"Expected 200 but got {response.status_code}"
)

    body = response.json()

    assert body["id"] == user_id