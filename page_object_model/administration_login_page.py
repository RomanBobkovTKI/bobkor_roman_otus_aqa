from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


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
        email_input = self.wait_element(self.EMAIL_INPUT)

        return email_input

    @property
    def email_label(self):
        email_label = self.wait_element(self.EMAIL_LABEL)

        return email_label

    @property
    def password_input(self):
        password_input = self.wait_element(self.PASSWORD_INPUT)

        return password_input

    @property
    def password_label(self):
        password_label = self.wait_element(self.PASSWORD_LABEL)

        return password_label

    @property
    def login_button(self):
        login_button = self.wait_element(self.LOGIN_BUTTON)

        return login_button

    @property
    def forgot_pass_link(self):
        link = self.wait_element(self.FORGOT_PASS_LINK)

        return link

    @property
    def reset_pass_button(self):
        button = self.wait_element(self.RESET_PASS_BUTTON)

        return button

    @property
    def stay_logged_in_label(self):
        label = self.wait_element(self.STAY_LOGIN_IN_LABEL)

        return label

    @property
    def login_logo(self):
        logo = self.wait_element(self.LOGIN_LOGO)

        return logo

    def click_to_forgot_pass(self):
        self.forgot_pass_link.click()

    def clear_email_input(self):
        self.email_input.clear()

    def clear_password_input(self):
        self.password_input.clear()

    def send_keys_to_email(self, email):
        self.email_input.send_keys(email)

    def send_keys_to_password(self, password):
        self.password_input.send_keys(password)

    def click_to_log_in_button(self):
        self.login_button.click()
