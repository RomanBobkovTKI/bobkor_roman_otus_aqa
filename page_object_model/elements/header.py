import re

from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class Header(BasePage):
    CONTACT_US = (By.CSS_SELECTOR, "#contact-link a")
    SEARCH_WIDGET = (By.CSS_SELECTOR, "#search_widget")
    WIDGET_INPUT_PLACEHOLDER = (
        By.CSS_SELECTOR,
        "#search_widget input[placeholder='Search our catalog']",
    )
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#_desktop_user_info span")
    SIGN_IN_LINK = (By.CSS_SELECTOR, "#_desktop_user_info a")
    CART_ELEMENT = (By.CSS_SELECTOR, "#_desktop_cart")
    LOGO_ELEMENT = (By.CSS_SELECTOR, "#_desktop_logo")
    LOGO_LINK = (By.CSS_SELECTOR, "#_desktop_logo a")
    CLOTHES_BUTTON = (By.CSS_SELECTOR, "#category-3")
    ACCESSORIES_BUTTON = (By.CSS_SELECTOR, "#category-6")
    CHANGE_CURRENCY_BUTTON = (By.CSS_SELECTOR, ".hidden-sm-down.btn-unstyle")
    DOLLAR_VALUE_IN_CURRENCY_OPTION = (By.CSS_SELECTOR, "a[title='US Dollar']")
    COUNT_ITEM_IN_CART = (By.CSS_SELECTOR, ".cart-products-count")

    @property
    def contact_us_link(self):
        link = self.wait_element(self.CONTACT_US)

        return link.get_attribute("href")

    @property
    def widget_input_element(self):
        return self.wait_element(self.SEARCH_WIDGET)

    @property
    def widget_input_placeholder(self):
        return self.wait_element(self.WIDGET_INPUT_PLACEHOLDER).get_attribute("placeholder")

    @property
    def sign_in_button(self):
        return self.wait_element(self.SIGN_IN_BUTTON)

    @property
    def cart_element(self):
        return self.wait_element(self.CART_ELEMENT)

    @property
    def logo_element(self):
        return self.wait_element(self.LOGO_ELEMENT)

    @property
    def logo_link_element(self):
        return self.wait_element(self.LOGO_LINK)

    @property
    def count_item_in_cart(self):
        count = self.wait_element(self.COUNT_ITEM_IN_CART).text
        return int(re.search(r"\d+", count).group())

    def click_contact_us_link(self):
        self.click(self.CONTACT_US)

    def click_to_sign_in_link(self):
        self.click(self.SIGN_IN_LINK)

    def click_to_logo(self):
        self.click(self.LOGO_ELEMENT)

    def click_to_clothes_button(self):
        self.click(self.CLOTHES_BUTTON)

    def click_to_accessories_button(self):
        self.click(self.ACCESSORIES_BUTTON)

    def click_to_change_currency_button(self):
        self.click(self.CHANGE_CURRENCY_BUTTON)

    def click_to_dollar_value_in_currency_option(self):
        self.click(self.DOLLAR_VALUE_IN_CURRENCY_OPTION)
