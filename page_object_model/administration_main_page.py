from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class AdministrationMainPage(BasePage):
    HEADER_DASHBOARD = (By.CSS_SELECTOR, "h1.page-title")
    PROFILE_ICON = (By.CSS_SELECTOR, "#employee_infos")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#header_logout")

    @property
    def dashboard_header(self):
        header = self.wait_element(self.HEADER_DASHBOARD, timeout=10)

        return header

    def click_to_profile_icon(self):
        icon = self.wait_element(self.PROFILE_ICON)
        icon.click()

    def click_logout_button(self):
        button = self.wait_element(self.LOGOUT_BUTTON)
        button.click()
