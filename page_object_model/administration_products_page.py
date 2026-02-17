from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class AdministrationProductsPage(BasePage):
    ADD_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#page-header-desc-configuration-add")
    ADD_NEW_PRODUCT_IN_MODAL = (By.CSS_SELECTOR, "#create_product_create")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#product_header_name_1")
    SUMMARY_TEXTAREA = (By.CSS_SELECTOR, "#product_description_description_short_1")
    DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, "#product_description_description_1")
    SAVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#product_footer_save")
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'Successful update')]")
    IFRAME = (By.CSS_SELECTOR, 'iframe[name="modal-create-product-iframe"]')

    @property
    def product_name_input(self):
        input_name = self.wait_element(self.PRODUCT_NAME)

        return input_name

    @property
    def product_summary_textarea(self):
        summary = self.wait_element(self.SUMMARY_TEXTAREA)

        return summary

    @property
    def product_description_input(self):
        input_description = self.wait_element(self.DESCRIPTION_TEXTAREA)

        return input_description

    @property
    def success_message(self):
        success_message = self.wait_element(self.SUCCESS_MESSAGE)

        return success_message

    def click_add_new_product(self):
        button = self.wait_element(self.ADD_NEW_PRODUCT_BUTTON)
        button.click()

    def click_add_new_product_in_modal(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it(self.IFRAME))

        button = self.wait_element(self.ADD_NEW_PRODUCT_IN_MODAL, timeout=10)
        button.click()

        self.driver.switch_to.default_content()

    def clear_product_name(self):
        self.product_name_input.clear()

    def send_keys_to_product_name(self, product_name):
        self.product_name_input.send_keys(product_name)

    def clear_product_summary_textarea(self):
        self.product_summary_textarea.clear()

    def send_keys_to_product_summary_textarea(self, product_summary_text):
        self.product_summary_textarea.send_keys(product_summary_text)

    def clear_product_description_input(self):
        self.product_description_input.clear()

    def send_keys_to_product_description_input(self, product_description_input):
        self.product_description_input.send_keys(product_description_input)

    def click_to_save_product_button(self):
        button = self.wait_element(self.SAVE_PRODUCT_BUTTON)
        button.click()
