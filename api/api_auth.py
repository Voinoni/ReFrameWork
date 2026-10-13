# auth_api.py

import requests

BASE_URL = "https://dummyjson.com"


def login(username, password):

    payload = {
        "username": username,
        "password": password
    }

    return requests.post(
        f"{BASE_URL}/auth/login",
        json=payload
    )