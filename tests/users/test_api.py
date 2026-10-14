from api.api_client import get_user

def test_get_user():
    response = get_user(2)

    assert response.status_code == 200