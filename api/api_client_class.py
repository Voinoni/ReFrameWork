from api.base_api import BaseApi


class UserApi(BaseApi):

    def get_user(self, user_id):

        return self.get(
            f"/users/{user_id}"
        )

    def search_user(self, search_text):

        return self.get(
            f"/users/search?q={search_text}"
        )

    def create_user(self, payload):

        return self.post(
            "/users/add",
            payload
        )

    def update_user(self, user_id, payload):

        return self.put(
            f"/users/{user_id}",
            payload
        )

    def delete_user(self, user_id):

        return self.delete(
            f"/users/{user_id}"
        )