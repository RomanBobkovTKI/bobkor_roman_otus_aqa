from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class SignInLoginModal(BasePage):
    MODAL_HEADER = (By.XPATH, "//h5[@class='modal-title' and text()='Sign in']")

    @property
    def header(self):
        return self.wait_element(self.MODAL_HEADER)
