import requests

def test_create_user(user_payload):

    response = requests.post(
        "https://dummyjson.com/users/add",
        json=user_payload
    )

    assert response.status_code == 201

    body = response.json()
    assert "id" in body
    print(body)
    #assert body["name"] == "Adam"