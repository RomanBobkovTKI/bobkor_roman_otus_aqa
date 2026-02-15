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

    @property
    def contact_us_link(self):
        link = self.wait_element(self.CONTACT_US)

        return link.get_attribute("href")

    @property
    def widget_input_element(self):
        element = self.wait_element(self.SEARCH_WIDGET)

        return element

    @property
    def widget_input_placeholder(self):
        placeholder = self.wait_element(self.WIDGET_INPUT_PLACEHOLDER)

        return placeholder.get_attribute("placeholder")

    @property
    def sign_in_button(self):
        button = self.wait_element(self.SIGN_IN_BUTTON)

        return button

    @property
    def cart_element(self):
        element = self.wait_element(self.CART_ELEMENT)

        return element

    @property
    def logo_element(self):
        element = self.wait_element(self.LOGO_ELEMENT)

        return element

    @property
    def logo_link_element(self):
        element = self.wait_element(self.LOGO_LINK)

        return element

    def click_contact_us_link(self):
        link = self.wait_element(self.CONTACT_US)
        link.click()

    def click_to_sign_in_link(self):
        link = self.wait_element(self.SIGN_IN_LINK)
        link.click()

    def click_to_logo(self):
        link = self.wait_element(self.LOGO_ELEMENT)
        link.click()