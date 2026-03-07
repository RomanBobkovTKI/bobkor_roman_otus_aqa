import logging

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)


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
        logger.debug(f"⏳ Waiting for element: {locator} (timeout: {timeout}s)")
        element = None

        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator[1]}")

        return element

    def wait_elements(self, locator: tuple[str, str], timeout: int = 4):
        logger.debug(f"⏳ Waiting for elements: {locator} (timeout: {timeout}s)")
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator[1]}")

    def click(self, locator: tuple[str, str]):
        logger.debug(f"⏳ Click for element: {locator}")
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"✅ Click successful on element: {locator}")
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator[1]}")
