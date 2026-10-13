import requests

def test_users_list():

    response = requests.get(
        "https://dummyjson.com/users"
    )

    body = response.json()

    assert len(body["users"]) > 0

    print("first value:", body["users"][0]["firstName"])
    #print(response.text)
    print("Seccond value:", body["users"][1]["firstName"])

    print("✅ End-to-End Test Passed")