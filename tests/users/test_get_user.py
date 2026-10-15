from api.base_api import BaseApi
import json

def test_get_user():

    api = BaseApi()

    response = api.get(
        "/users/1"
    )

    assert response.status_code == 200, (
        f"Expected 200 but got {response.status_code}"
    )

    body = response.json()

    assert body["id"] == 1
    
    assert body["firstName"] == "Emily"
    assert body["lastName"] == "Johnson"
    #------Add more validations----------
    assert body["gender"] == "female"
    assert body["role"] == "admin"
    assert "@" in body["email"]
    assert body["address"]["city"] == "Phoenix"
    assert body["address"]["state"] == "Mississippi"
    #-----print full body------
    #print(body)
    #--------------------------
    print("ID:", body["id"])
    #------------test view body----------------------
    print("First Name:", body["firstName"])
    print("Last Name:", body["lastName"])
    
    
    #------------test view body json Format----------
    #print(json.dumps(body, indent=4))
    #print(response.json())
    #------------Show All Keys-----------------------
    #print(body.keys())
    #-------Inspect Response Before JSON-------------
    print(response.status_code)
    #print(response.headers)
    print(response.text)
    