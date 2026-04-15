import os
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from fixtures.url import presta_shop_url
from fixtures.logger import configure_logging

logger = logging.getLogger(__name__)


@pytest.fixture()
def driver(request, presta_shop_url, configure_logging):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    executor = request.config.getoption("--executor")

    if executor:
        logger.info(f"🌐 Using remote executor: {executor}")

        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        options.set_capability("browserName", "chrome")
        options.set_capability("selenoid:options", {
            "screenResolution": "1920x1080x24",
            "enableVNC": True,
            "enableVideo": False,
            "name": request.node.name
        })
        logger.info(f"🔗 Using base URL: {presta_shop_url}")
        driver: WebDriver = webdriver.Remote(
            command_executor=f"{executor}/wd/hub",
            options=options,
        )

    else:
        if browser_name == "chrome":
            options = ChromeOptions()
            service = ChromeService()

            if headless or os.getenv("IS_DOCKER"):
                options.add_argument("--headless=new")

            if os.getenv("IS_DOCKER"):
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
                service = ChromeService(executable_path="/usr/bin/chromedriver")
                logger.info("🐳 FROM DOCKER (local Chrome)")

            options.page_load_strategy = "eager"
            driver = webdriver.Chrome(options=options, service=service)

        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)

        elif browser_name == "safari":
            if headless:
                pytest.skip("Safari does not support headless mode")
            driver = webdriver.Safari()

        else:
            pytest.fail(f"❌ Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)
    driver.get(presta_shop_url)
    logger.info(f"🔓 Opening: {presta_shop_url}")

    yield driver

    logger.info("🔒 Quitting driver")
    driver.quit()