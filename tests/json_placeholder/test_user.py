import os

import requests

import pytest

from services.user_generate import get_user

url = os.getenv("JSON_PLACEHOLDER_URL")
user_url = "users"


@pytest.mark.json
@pytest.mark.json_user
@pytest.mark.parametrize(
    "status_code",
    [
        requests.codes.ok,
    ],
    ids=["status_code 200"],
)
def test_get_users(status_code):
    response = requests.get(f"{url}/{user_url}")

    assert response.status_code == status_code, (
        f"response status_code: {response.status_code} == status_code"
    )
    assert len(response.json()) != 0, f"users is not empty"


@pytest.mark.json
@pytest.mark.json_user
@pytest.mark.parametrize(
    ("user_id", "status_code"),
    [
        pytest.param(1, 200, id="get user by id = 1"),
        pytest.param(2, 200, id="get user by id = 2"),
        pytest.param(10, 200, id="get user by id = 2"),
    ],
)
def test_get_user_by_id(user_id, status_code):
    response = requests.get(f"{url}/{user_url}/{user_id}")
    user = response.json()

    assert response.status_code == status_code, f"{response.status_code} == 200"
    assert user.get("id") == user_id, f"user_id: {user.get('id')} == {user_id}"


@pytest.mark.json
@pytest.mark.json_user
@pytest.mark.parametrize(
    ("user_id", "status_code"),
    [
        pytest.param(11, 404, id="get user by id = 11"),
        pytest.param(124, 404, id="get user by id = 124"),
        pytest.param(1334, 404, id="get user by id = 1334"),
    ],
)
def test_not_found_user(user_id, status_code):
    response = requests.get(f"{url}/{user_url}/{user_id}")

    assert response.status_code == status_code, (
        f"user not found, status_code {status_code}"
    )


@pytest.mark.json
@pytest.mark.json_user
def test_create_user():
    response = requests.post(f"{url}/{user_url}", data=get_user())

    assert response.status_code == 201, f"create user"


@pytest.mark.json
@pytest.mark.json_user
@pytest.mark.parametrize(
    ("user_id", "status_code"),
    [
        pytest.param(1, 200, id="delete user by id = 1"),
        pytest.param(10, 200, id="delete user by id = 10"),
        pytest.param(101, 200, id="delete user by id = 101"),
    ],
)
def test_delete_user(user_id, status_code):
    response = requests.delete(f"{url}/{user_url}/{user_id}")

    assert response.status_code == status_code, f"delete user by id {user_id}"
