import pytest
import requests


@pytest.fixture(scope="session")
def url_fixture(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="session")
def status_code_fixture(request):
    return request.config.getoption("--status_code")

def test_status_code(url_fixture, status_code_fixture):
    response = requests.get(url_fixture)

    assert response.status_code == int(status_code_fixture)