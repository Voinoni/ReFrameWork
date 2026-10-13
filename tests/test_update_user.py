import requests

def test_update_user():

    payload = {
        "firstName": "Adam"
    }

    response = requests.put(
        "https://dummyjson.com/users/1",
        json=payload
    )
    
    assert response.status_code == 200

    data = response.json()

    print(data)
    print(response.json())
    assert data["firstName"] == "Adam"