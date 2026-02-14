from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, locator: tuple[str, str], timeout: int = 4):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator[1]}")

    def wait_elements(self, locator: tuple[str, str], timeout: int = 4):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator[1]}")