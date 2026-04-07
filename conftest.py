from dotenv import load_dotenv
import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

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

    parser.addoption(
        "--executor",
        action="store",
        default=None,
        help="Selenoid executor URL (e.g., http://selenoid:4444/wd/hub)"
    )

    parser.addoption(
        "--browser_version",
        action="store",
        default=None,
        help="Browser version for Selenoid (e.g., 120.0)"
    )

    parser.addoption(
        "--opencart_url",
        action="store",
        default=None,
        help="URL of the PrestaShop instance",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        for fixture in item.funcargs.values():
            if isinstance(fixture, WebDriver):
                screenshot = fixture.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name=f"failure_{item.name}",
                    attachment_type=allure.attachment_type.PNG,
                )
                break
