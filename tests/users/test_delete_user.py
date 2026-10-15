from api.base_api import BaseApi


def test_delete_user():

    api = BaseApi()

    response = api.delete(
        "/users/1"
    )

    assert response.status_code == 200

    body = response.json()

    print(body)

    assert body["id"] == 1
    assert body["isDeleted"] is True