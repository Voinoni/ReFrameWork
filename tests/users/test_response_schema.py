import requests


def test_response_schema():

    response = requests.get(
        "https://dummyjson.com/users/1"
    )

    body = response.json()

    #assert "data" in body
    #assert "id" in body["data"]
    #assert "email" in body["data"]
    #assert "first_name" in body["data"]
    #-------new-------
    assert "id" in body
    assert "firstName" in body
    assert "lastName" in body
    assert "email" in body