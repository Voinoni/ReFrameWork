import pytest
from api.base_api import BaseApi

@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_users(user_id):

    api = BaseApi()
    response = api.get(
        f"/users/{user_id}"
    )

    assert response.status_code == 200