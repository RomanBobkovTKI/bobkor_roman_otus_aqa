import os

import pytest


@pytest.fixture(scope="function")
def presta_shop_url(request) -> str:
    executor = request.config.getoption("--executor")

    path = getattr(request, "param", None)

    opencart_url = request.config.getoption("--opencart_url")
    if opencart_url:
        if path:
            base = opencart_url.rstrip('/')
            path_clean = path.lstrip('/')
            return f"{base}/{path_clean}"
        return opencart_url

    protocol = os.getenv("HTTP", "http")
    port = os.getenv("SHOP_PORT", "8081")
    host = request.config.getoption("--url")

    if host == "default":
        host = os.getenv("LOCALHOST", "localhost")

    url = f"{protocol}://{host}:{port}"

    if path is not None:
        url = f"{url}/{path}"

    if executor:
        return "http://prestashop"

    return url

