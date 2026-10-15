import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "https://dummyjson.com"


@pytest.fixture
def login_credentials():
    return {
        "username": "emilys",
        "password": "emilyspass"
    }


@pytest.fixture
def auth_token(base_url, login_credentials):

    response = requests.post(
        f"{base_url}/auth/login",
        json=login_credentials
    )

    assert response.status_code == 200

    return response.json()["accessToken"]


@pytest.fixture
def user_payload():
    return {
        "firstName": "Adam",
        "lastName": "Voinoni"
    }