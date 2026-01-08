import os

import pytest

from services.auth_service import AuthService

login = os.environ.get("LOGIN")
password = os.environ.get("PASSWORD")
jwt_url = os.environ.get("JWT_URL")

@pytest.fixture(scope="session")
def get_token(request):
    auth_service = AuthService(base_url=jwt_url)
    token = auth_service.login(username=login, password=password)
    return token

@pytest.fixture(scope="module")
def auth_service(get_token):
    return AuthService(base_url=jwt_url, token=get_token)

@pytest.mark.auth
def test_get_secure_data(auth_service):
    response = auth_service.get_data()

    assert "success" in response
    assert response.get("success") == "my secure data"
