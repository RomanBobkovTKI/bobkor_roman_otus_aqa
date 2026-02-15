from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class MainPage(BasePage):
    FIRST_CURRENCY_PRICE = (By.CSS_SELECTOR, ".price")

    @property
    def currency_price_element(self):
        currency_price = self.wait_element(self.FIRST_CURRENCY_PRICE)

        return currency_price
