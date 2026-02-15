from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class WomenCategories(BasePage):
    HEADER = (By.CSS_SELECTOR, "h1")

    @property
    def header(self):
        header = self.wait_element(self.HEADER)

        return header
