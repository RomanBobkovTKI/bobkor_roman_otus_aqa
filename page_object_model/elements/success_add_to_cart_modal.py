from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class SuccessAddToCartModal(BasePage):
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, ".modal-header .close .material-icons")

    def click_to_close_modal(self):
        self.click(self.CLOSE_MODAL_BUTTON)
