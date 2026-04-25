import pytest


@pytest.fixture(scope="function", autouse=True)
def open_app(appium_driver):
    appium_driver.terminate_app("com.csdroid.pkg")
    appium_driver.activate_app("com.csdroid.pkg")
