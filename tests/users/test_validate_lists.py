from api.base_api import BaseApi


def test_users_list():

    api = BaseApi()

    response = api.get(
        "/users/"
    )

    body = response.json()

    assert len(body["users"]) > 0

    print("first value:", body["users"][0]["firstName"])
    #print(response.text)
    print("Seccond value:", body["users"][1]["firstName"])

    print("✅ End-to-End Test Passed")