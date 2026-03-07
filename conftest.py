from dotenv import load_dotenv

from fixtures.url import presta_shop_url
from fixtures.driver import driver
from fixtures.logger import configure_logging


def pytest_configure():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="choose browser: chrome, firefox or safari",
    )

    parser.addoption(
        "--url",
        action="store",
        default="default",
        help="url of PrestaShop",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="run in headless mode",
    )

    parser.addoption(
        "--app-log-level",
        action="store",
        default="INFO",
        help="Уровень логирования: DEBUG, INFO, WARNING, ERROR",
    )
