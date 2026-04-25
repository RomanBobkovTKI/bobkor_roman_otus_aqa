import pytest
from appium.options.common import AppiumOptions
from appium import webdriver


@pytest.fixture(scope="session")
def appium_driver():
    options = AppiumOptions()
    options.load_capabilities(
        {
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:newCommandTimeout": 3600,
            "appPackage": "com.csdroid.pkg",
            "appActivity": ".MainActivity",
        }
    )

    appium_server_url = "http://127.0.0.1:4723"

    android_driver = webdriver.Remote(
        command_executor=appium_server_url, options=options
    )
    android_driver.implicitly_wait(10)
    yield android_driver
    android_driver.quit()
