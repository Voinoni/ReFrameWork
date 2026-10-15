from api.api_client_class import UserApi


def test_update_user():

    api = UserApi()

    payload = {
        "firstName": "Adam"
    }

    response = api.update_user(
        1,
        payload
    )

    api = UserApi()

    print(dir(api))
    
    assert response.status_code == 200

    data = response.json()

    print(data)
    print(response.json())
    assert data["firstName"] == "Adam"

    