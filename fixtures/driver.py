import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        pass
    elif browser_name == "safari":
        pass
    elif browser_name == "yandex":
        pass

    yield driver

    driver.quit()
