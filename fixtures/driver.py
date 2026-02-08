import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = ChromeOptions()

        if headless:
            options.add_argument("--headless")

        options.page_load_strategy = 'eager'
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

    yield driver

    driver.quit()
