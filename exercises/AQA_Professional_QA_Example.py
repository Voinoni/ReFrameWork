import requests

def test_get_user():

    url = "https://reqres.in/api/users/2"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"

    print("✅ API Validation Passed")


test_get_user()