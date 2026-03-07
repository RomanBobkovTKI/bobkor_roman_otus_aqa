import pytest

from logging_config import setup_logging


@pytest.fixture()
def configure_logging(request):
    log_level = request.config.getoption("--app-log-level")
    setup_logging(log_level=log_level)
