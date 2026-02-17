from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class RegistrationPage(BasePage):
    URL = "registration"

    HEADER = (By.CSS_SELECTOR, ".page-header h1")
    HAVE_ACCOUNT_LINK = (By.XPATH, "//section//a[contains(@href, 'login')]")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#field-firstname")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#field-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#field-email")
    SAVE_BUTTON = (By.XPATH, "//button[contains(@type, 'submit')]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#field-password")
    BIRTHDAY_INPUT = (By.CSS_SELECTOR, "#field-birthday")
    CHECKBOX_PRIVACY_INPUT = (By.CSS_SELECTOR, "input[name='psgdpr']")
    CHECKBOX_PRIVACY_DATA = (By.CSS_SELECTOR, "input[name = 'customer_privacy']")

    @property
    def header (self):
        header = self.wait_element(self.HEADER)

        return header

    @property
    def first_name_input(self):
        fn_input = self.wait_element(self.FIRST_NAME_INPUT)

        return fn_input

    @property
    def last_name_input(self):
        last_name_input = self.wait_element(self.LAST_NAME_INPUT)

        return last_name_input

    @property
    def email_input(self):
        email_input = self.wait_element(self.EMAIL_INPUT)

        return email_input

    @property
    def password_input(self):
        password_input = self.wait_element(self.PASSWORD_INPUT)

        return password_input

    @property
    def birthday_input(self):
        birthday_input = self.wait_element(self.BIRTHDAY_INPUT)

        return birthday_input

    @property
    def checkbox_privacy_input(self):
        checkbox = self.wait_element(self.CHECKBOX_PRIVACY_INPUT)

        return checkbox

    @property
    def checkbox_privacy_data_input(self):
        checkbox = self.wait_element(self.CHECKBOX_PRIVACY_DATA)

        return checkbox

    def click_to_log_in_instead(self):
        link = self.wait_element(self.HAVE_ACCOUNT_LINK)
        link.click()

    def clear_first_name_input(self):
        fn_input = self.wait_element(self.FIRST_NAME_INPUT)
        fn_input.clear()

    def click_to_save_button(self):
        button = self.wait_element(self.SAVE_BUTTON)
        button.click()

    def send_keys_to_first_name_input(self, first_name):
        self.first_name_input.send_keys(first_name)

    def clear_last_name_input(self):
        self.last_name_input.clear()

    def send_keys_to_last_name_input(self, last_name):
        self.last_name_input.send_keys(last_name)

    def clear_email_input(self):
        self.email_input.clear()

    def send_keys_to_email_input(self, email):
        self.email_input.send_keys(email)

    def clear_password_input(self):
        self.password_input.clear()

    def send_keys_to_password_input(self, password):
        self.password_input.send_keys(password)

    def clear_birthday_input(self):
        self.birthday_input.clear()

    def send_keys_to_birthday_input(self, birthday):
        self.birthday_input.send_keys(birthday)

    def click_to_checkbox_privacy_input(self):
        checkbox = self.checkbox_privacy_input
        checkbox.click()

    def click_to_checkbox_privacy_data_input(self):
        self.checkbox_privacy_data_input.click()