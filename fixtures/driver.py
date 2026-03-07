import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from fixtures.url import presta_shop_url
from fixtures.logger import configure_logging

logger = logging.getLogger(__name__)


@pytest.fixture()
def driver(request, presta_shop_url, configure_logging):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = ChromeOptions()

        if headless:
            options.add_argument("--headless")

        options.page_load_strategy = "eager"
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
    elif browser_name == "safari":
        if headless:
            pytest.skip("Skipping headless browser")

        driver = webdriver.Safari()
    elif browser_name == "yandex":
        service = Service(executable_path="/Users/Bobkov.Roman5/Documents/yandexdriver")
        options = ChromeOptions()
        options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Chrome(service=service, options=options)
    else:
        pytest.fail(f"Unsupported browser {browser_name}")

    driver.implicitly_wait(2)
    driver.get(presta_shop_url)
    logger.info(f"🔓 Opening page: {presta_shop_url}")

    yield driver

    logger.info("🔒 Quitting driver")
    driver.quit()
