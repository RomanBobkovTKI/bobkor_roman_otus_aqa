from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class SuccessAddToCartModal(BasePage):
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, ".modal-header .close .material-icons")

    def click_to_close_modal(self):
        button = self.wait_element(self.CLOSE_MODAL_BUTTON)
        button.click()
