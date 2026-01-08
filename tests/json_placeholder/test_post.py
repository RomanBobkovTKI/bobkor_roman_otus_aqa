import os

import pytest
import requests

from services.post_generate import get_random_post

url = os.getenv("JSON_PLACEHOLDER_URL")
post_url = "posts"


@pytest.mark.json
@pytest.mark.json_post
@pytest.mark.parametrize(
    "status_code",
    [
        requests.codes.ok,
    ],
    ids=["status_code 200"],
)
def test_get_posts(status_code):
    response = requests.get(f"{url}/{post_url}")

    assert response.status_code == status_code, f"response status_code: {status_code}"
    assert response.json() != [], f"posts is not empty"


@pytest.mark.json
@pytest.mark.json_post
@pytest.mark.parametrize(
    ["post_id", "status_code"],
    [
        pytest.param(1, 200, id="get post by id = 1"),
        pytest.param(24, 200, id="get post by id = 24"),
        pytest.param(100, 200, id="get post by id = 100"),
    ],
)
def test_get_post_by_id(post_id, status_code):
    response = requests.get(f"{url}/{post_url}/{post_id}")
    post = response.json()

    assert response.status_code == status_code, f"get post by id = {id}"
    assert post.get("id") == post_id, f"post id: {post.get('id')} == {post_id}"


@pytest.mark.json
@pytest.mark.json_post
@pytest.mark.parametrize(
    ["post_id", "status_code"],
    [
        pytest.param(123, 404, id="get post by id = 123"),
        pytest.param(1230, 404, id="get post by id = 1230"),
    ],
)
def test_not_found_post(post_id, status_code):
    response = requests.get(f"{url}/{post_url}/{post_id}")

    assert response.status_code == status_code, (
        f"post not found, status_code {status_code}"
    )


@pytest.mark.json
@pytest.mark.json_post
def test_create_post():
    response = requests.post(f"{url}/{post_url}", data=get_random_post())

    assert response.status_code == 201, f"create post"


@pytest.mark.json
@pytest.mark.json_post
@pytest.mark.parametrize(
    ["post_id", "status_code"],
    [
        pytest.param(1, 200, id="delete post by id = 1"),
        pytest.param(24, 200, id="delete post by id = 24"),
    ],
)
def test_delete_post(post_id, status_code):
    response = requests.delete(f"{url}/{post_url}/{post_id}")

    assert response.status_code == status_code, f"delete post by id {post_id}"
