import random

from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


class ProductCard(BasePage):
    BREADCRUMBS_PRODUCT_NAME = (By.CSS_SELECTOR, ".breadcrumb ol li:last-child")
    HEADER = (By.CSS_SELECTOR, "h1")
    PRICE = (By.CSS_SELECTOR, ".current-price-value")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart")
    FB_ICON = (By.CSS_SELECTOR, ".facebook.icon-gray")
    X_ICON = (By.CSS_SELECTOR, ".twitter.icon-gray")
    PINTEREST_ICON = (By.CSS_SELECTOR, ".pinterest.icon-gray")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, ".wishlist-button-add.wishlist-button-product")

    @property
    def product_name_from_breadcrumbs(self):
        breadcrumbs = self.wait_element(self.BREADCRUMBS_PRODUCT_NAME)

        return breadcrumbs

    @property
    def header_card_name(self):
        header = self.wait_element(self.HEADER)

        return header

    @property
    def price(self):
        price = self.wait_element(self.PRICE)

        return price

    @property
    def add_to_cart_button(self):
        button = self.wait_element(self.ADD_TO_CART_BUTTON)

        return button

    @property
    def facebook_icon(self):
        icon = self.wait_element(self.FB_ICON)

        return icon

    @property
    def x_icon(self):
        icon = self.wait_element(self.X_ICON)

        return icon

    @property
    def pinterest_icon(self):
        icon = self.wait_element(self.PINTEREST_ICON)

        return icon

    @property
    def wishlist_button(self):
        button = self.wait_element(self.WISHLIST_BUTTON)

        return button

    def click_to_add_to_cart(self):
        button = self.wait_element(self.ADD_TO_CART_BUTTON)
        button.click()

    def click_to_add_to_wishlist(self):
        button = self.wait_element(self.WISHLIST_BUTTON)
        button.click()
