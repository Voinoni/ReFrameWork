# api/base_api.py

import requests


class BaseApi:

    BASE_URL = "https://dummyjson.com"

#    def get(self, endpoint):
#       return requests.get(
#            f"{self.BASE_URL}{endpoint}"
#        )

#    def post(self, endpoint, payload):
#        return requests.post(
#            f"{self.BASE_URL}{endpoint}",
#            json=payload
#        )
    def get(
    self,
    endpoint,
    headers=None
    ):

        return requests.get(
            f"{self.BASE_URL}{endpoint}",
            headers=headers
        )
    def post(
    self,
    endpoint,
    payload,
    headers=None
    ):

        return requests.post(
            f"{self.BASE_URL}{endpoint}",
            json=payload,
            headers=headers
        )
    def put(self, endpoint, payload):
        return requests.put(
            f"{self.BASE_URL}{endpoint}",
            json=payload
        )

    def delete(self, endpoint):
        return requests.delete(
            f"{self.BASE_URL}{endpoint}"
        )
