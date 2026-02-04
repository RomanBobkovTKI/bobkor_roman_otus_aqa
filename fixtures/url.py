import os

import pytest


@pytest.fixture()
def presta_shop_url(request):
    protocol = os.getenv("HTTP")
    port = os.getenv("SHOP_PORT")
    host = request.config.getoption("--url")

    if host == "default":
        host = os.getenv("LOCALHOST")

    url = f"{protocol}://{host}:{port}"

    return url
