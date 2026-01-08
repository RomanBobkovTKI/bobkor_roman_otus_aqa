from services.base_client import BaseClient


class AuthService(BaseClient):
    def login(self, username: str, password: str):
        response = self.post("token", json={"login": username, "password": password})
        access_token= response.json().get("access_token")

        if not access_token:
            raise ValueError("invalid token or refresh token")

        return access_token

    def get_data(self):
        response = self.get("data")
        data = response.json()

        return data
