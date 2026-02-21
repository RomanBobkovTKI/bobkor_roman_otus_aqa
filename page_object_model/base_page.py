from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    @property
    def driver(self):
        return self._driver

    @property
    def current_url(self):
        return self._driver.current_url

    @property
    def title(self):
        return self._driver.title

    @property
    def wait(self):
        return self._wait

    def wait_element(self, locator: tuple[str, str], timeout: int = 4):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator[1]}")
            return None

    def wait_elements(self, locator: tuple[str, str], timeout: int = 4):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator[1]}")

    def click(self, locator: tuple[str, str]):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator[1]}")
