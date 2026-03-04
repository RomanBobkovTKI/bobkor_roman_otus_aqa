import os

import pytest


@pytest.fixture(scope="function")
def presta_shop_url(request) -> str:
    path = getattr(request, "param", None)

    protocol = os.getenv("HTTP")
    port = os.getenv("SHOP_PORT")
    host = request.config.getoption("--url")

    if host == "default":
        host = os.getenv("LOCALHOST")

    url = f"{protocol}://{host}:{port}"

    if path is not None:
        url = f"{url}/{path}"

    return url
