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
        return self.wait_element(self.HEADER_DASHBOARD, timeout=10)

    def click_to_profile_icon(self):
        self.click(self.PROFILE_ICON)

    def click_logout_button(self):
        self.click(self.LOGOUT_BUTTON)

    def click_to_subtab_admin_catalog(self):
        self.click(self.SUBTAB_ADMIN_CATALOG)

    def click_to_subtab_admin_products(self):
        self.click(self.SUBTAB_ADMIN_PRODUCTS)
