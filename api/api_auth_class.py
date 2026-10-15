# api/api_auth_class.py

import requests


class AuthApi:

    BASE_URL = "https://dummyjson.com"

    def login(self, username, password):

        payload = {
            "username": username,
            "password": password
        }

        return requests.post(
            f"{self.BASE_URL}/auth/login",
            json=payload
        )
    
    def create_user(self, payload):

        return self.post(
            "/users/add",
            payload
        )
