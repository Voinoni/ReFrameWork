from api.base_api import BaseApi


def test_retry_after_header():
    api = BaseApi()

    response = api.get(
        "/users/1"
    )

    if response.status_code == 429:
        assert "Retry-After" in response.headers