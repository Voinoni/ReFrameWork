import requests

class UserApi:

    BASE_URL = "https://dummyjson.com"

    def get_user(self, user_id):
        return requests.get(
            f"{self.BASE_URL}/users/{user_id}"
        )
    #----------Create Search User API----------#
    def search_user(self, search_text):
        return requests.get(
        f"{self.BASE_URL}/users/search?q={search_text}"
    )