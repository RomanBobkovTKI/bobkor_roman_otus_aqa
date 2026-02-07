from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element(selector, driver, timeout=4, by=By.CSS_SELECTOR):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )
    except TimeoutException:
        raise AssertionError(f"Не дождался видимости элемента: {selector}")


def wait_elements(selector, driver, timeout=4, by=By.CSS_SELECTOR):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_all_elements_located((by, selector))
        )
    except TimeoutException:
        raise AssertionError(f"Не дождался видимости элемента: {selector}")
