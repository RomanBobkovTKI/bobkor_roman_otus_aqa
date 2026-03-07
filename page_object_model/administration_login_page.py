import logging

from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage

logger = logging.getLogger(__name__)


class AdministrationPage(BasePage):
    URL = "administration/login?_token="

    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    EMAIL_LABEL = (By.CSS_SELECTOR, "label[for='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#passwd")
    PASSWORD_LABEL = (By.CSS_SELECTOR, "label[for='passwd']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#submit_login")
    FORGOT_PASS_LINK = (By.CSS_SELECTOR, "#forgot-password-link")
    RESET_PASS_BUTTON = (
        By.CSS_SELECTOR,
        "#request_password_reset_buttons_submit_login",
    )
    STAY_LOGIN_IN_LABEL = (By.CSS_SELECTOR, ".md-checkbox label")
    LOGIN_LOGO = (By.CSS_SELECTOR, "#shop-img")

    @property
    def email_input(self):
        return self.wait_element(self.EMAIL_INPUT)

    @property
    def email_label(self):
        return self.wait_element(self.EMAIL_LABEL)

    @property
    def password_input(self):
        return self.wait_element(self.PASSWORD_INPUT)

    @property
    def password_label(self):
        return self.wait_element(self.PASSWORD_LABEL)

    @property
    def login_button(self):
        return self.wait_element(self.LOGIN_BUTTON)

    @property
    def forgot_pass_link(self):
        return self.wait_element(self.FORGOT_PASS_LINK)

    @property
    def reset_pass_button(self):
        return self.wait_element(self.RESET_PASS_BUTTON)

    @property
    def stay_logged_in_label(self):
        return self.wait_element(self.STAY_LOGIN_IN_LABEL)

    @property
    def login_logo(self):
        return self.wait_element(self.LOGIN_LOGO)

    def click_to_forgot_pass(self):
        self.click(self.FORGOT_PASS_LINK)

    def clear_email_input(self):
        logger.debug(f"Clear input: {self.email_input}")
        self.email_input.clear()

    def clear_password_input(self):
        logger.debug(f"Clear input: {self.password_input}")
        self.password_input.clear()

    def send_keys_to_email(self, email):
        logger.info(f"Send keys to email: {email}")
        self.email_input.send_keys(email)

    def send_keys_to_password(self, password):
        logger.info(f"Send keys to password: {password}")
        self.password_input.send_keys(password)

    def click_to_log_in_button(self):
        self.click(self.LOGIN_BUTTON)
