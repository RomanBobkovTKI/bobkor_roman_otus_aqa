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
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'Successful')]")
    IFRAME = (By.CSS_SELECTOR, 'iframe[name="modal-create-product-iframe"]')
    ACTIONS_BUTTON_DIS = (By.CSS_SELECTOR, ".btn-group button[disabled]")
    ACTION_BUTTON = (By.CSS_SELECTOR, ".js-bulk-actions-btn")
    MD_CHECKBOX = (By.CSS_SELECTOR, ".md-checkbox")
    DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#product_grid_bulk_action_bulk_delete_ajax")
    DELETE_PRODUCT_IN_MODAL = (By.XPATH, '//button[contains(text(), "Delete selection")]')
    CLOSE_BUTTON = (By.XPATH, '//div[contains(@role, "dialog")]//button[contains(text(), "Close")]')

    @property
    def product_name_input(self):
        return self.wait_element(self.PRODUCT_NAME)

    @property
    def product_summary_textarea(self):
        return self.wait_element(self.SUMMARY_TEXTAREA)

    @property
    def product_description_input(self):
        return self.wait_element(self.DESCRIPTION_TEXTAREA)

    @property
    def success_message(self):
        return self.wait_element(self.SUCCESS_MESSAGE)


    def click_add_new_product(self):
        self.click(self.ADD_NEW_PRODUCT_BUTTON)

    def click_add_new_product_in_modal(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it(self.IFRAME))

        self.click(self.ADD_NEW_PRODUCT_IN_MODAL)
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
        self.click(self.SAVE_PRODUCT_BUTTON)

    def actions_button_is_disabled(self):
        actions_button = self.wait_element(self.ACTIONS_BUTTON_DIS)
        return actions_button.get_attribute("disabled") is not None

    def click_to_first_checkbox(self):
        button = self.wait_elements(self.MD_CHECKBOX)
        button[1].click()

    def click_to_actions_button_dis(self):
        self.click(self.ACTIONS_BUTTON_DIS)

    def click_to_actions_button(self):
        self.click(self.ACTION_BUTTON)

    def click_to_delete_product_button(self):
        self.click(self.DELETE_PRODUCT_BUTTON)

    def click_to_delete_product_in_modal(self):
        self.click(self.DELETE_PRODUCT_IN_MODAL)

    def click_to_close_button(self):
        self.click(self.CLOSE_BUTTON)