import requests

def test_response_headers():

    response = requests.get(
        "https://dummyjson.com/users/1"
    )

    assert response.status_code == 200

    assert "application/json" in response.headers["Content-Type"]