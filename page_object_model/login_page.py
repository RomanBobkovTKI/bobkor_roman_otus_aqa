from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class LoginPage(BasePage):
    HEADER = (By.CSS_SELECTOR, ".page-header h1")

    @property
    def header_element(self):
        return self.wait_element(self.HEADER)
