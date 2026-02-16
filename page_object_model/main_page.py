import random

from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class MainPage(BasePage):
    FIRST_CURRENCY_PRICE = (By.CSS_SELECTOR, ".price")
    PRODUCT_CARD = (By.CSS_SELECTOR, ".thumbnail.product-thumbnail")

    @property
    def currency_price_element(self):
        currency_price = self.wait_element(self.FIRST_CURRENCY_PRICE)

        return currency_price

    def click_to_random_product_card(self):
        buttons = self.wait_elements(self.PRODUCT_CARD)
        buttons[random.randint(0, len(buttons) - 1)].click()
