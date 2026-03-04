from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage
from utils.text_from_lement_list import get_text_from_element_list


class ClothesPage(BasePage):
    URL = "3-clothes"

    HEADER = (By.CSS_SELECTOR, "h1")
    ALL_BREADCRUMBS_TEXT = (By.CSS_SELECTOR, ".breadcrumb span")
    SUBCATEGORIES_HEADER = (By.CSS_SELECTOR, ".subcategory-heading")
    ALL_SUBCATEGORIES = (By.CSS_SELECTOR, ".subcategory-name")
    MEN_CATEGORIES_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'subcategory-image')]//a[contains(@href, '4-men')]",
    )
    WOMEN_CATEGORIES_LINK = (By.CSS_SELECTOR, "a[title='Women']")

    @property
    def header(self):
        return self.wait_element(self.HEADER)

    @property
    def breadcrumbs_text_list(self):
        breadcrumbs_list = self.wait_elements(self.ALL_BREADCRUMBS_TEXT)
        breadcrumbs_text = get_text_from_element_list(breadcrumbs_list)

        return breadcrumbs_text

    @property
    def subcategories_header(self):
        return self.wait_element(self.SUBCATEGORIES_HEADER)

    @property
    def all_subcategories_list(self):
        subcategories_list = self.wait_elements(self.ALL_SUBCATEGORIES)
        subcategories_text = get_text_from_element_list(subcategories_list)

        return subcategories_text

    @property
    def header_text(self):
        return self.wait_element(self.HEADER).text

    def click_to_men_categories_button(self):
        self.click(self.MEN_CATEGORIES_BUTTON)

    def click_to_women_categories_link(self):
        self.click(self.WOMEN_CATEGORIES_LINK)
