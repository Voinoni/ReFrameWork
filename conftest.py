import pytest

@pytest.fixture
def base_url():
    #return "https://reqres.in/api"
    return "https://dummyjson.com"

@pytest.fixture
def user_payload():
    return {
        "firstName": "Adam"
        #"job": "QA Engineer"
    }