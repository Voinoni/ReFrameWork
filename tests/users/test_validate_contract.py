from api.api_client import get_user


def test_validate_contract():

    response = get_user(1)

    body = response.json()

    expected_fields = [
        "id",
        "email",
        "firstName",
        "lastName"
    ]

    for field in expected_fields:
        assert field in body