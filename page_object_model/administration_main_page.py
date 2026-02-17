from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class AdministrationMainPage(BasePage):
    HEADER_DASHBOARD = (By.CSS_SELECTOR, "h1.page-title")
    PROFILE_ICON = (By.CSS_SELECTOR, "#employee_infos")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#header_logout")
    SUBTAB_ADMIN_CATALOG = (By.CSS_SELECTOR, "#subtab-AdminCatalog")
    SUBTAB_ADMIN_PRODUCTS = (By.CSS_SELECTOR, "#subtab-AdminProducts")

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

    def click_to_subtab_admin_catalog(self):
        button = self.wait_element(self.SUBTAB_ADMIN_CATALOG)
        button.click()

    def click_to_subtab_admin_products(self):
        button = self.wait_element(self.SUBTAB_ADMIN_PRODUCTS)
        button.click()
