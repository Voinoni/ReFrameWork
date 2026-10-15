# api/api_client_class.py
from api.api_client_class import UserApi


def test_create_user(user_payload):

    api = UserApi()

    response = api.create_user(
        user_payload
    )

    assert response.status_code == 201

    body = response.json()

    assert "id" in body
    print(body)
    #assert body["name"] == "Adam"