import os

import pytest


@pytest.fixture()
def presta_shop_url():
    protocol = os.getenv("HTTP")
    host = os.getenv("LOCALHOST")
    port = os.getenv("SHOP_PORT")

    url = f"{protocol}://{host}:{port}"

    return url
