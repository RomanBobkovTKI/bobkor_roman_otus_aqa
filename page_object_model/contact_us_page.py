from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class ContactUs(BasePage):
    HEADER = (By.CSS_SELECTOR, ".form-fields h3")

    @property
    def header_page_text(self):
        return self.wait_element(self.HEADER).text
