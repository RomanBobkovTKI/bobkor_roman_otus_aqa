from selenium.webdriver.common.by import By

from page_object_model.base_page import BasePage


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
        header = self.wait_element(self.HEADER)

        return header

    @property
    def breadcrumbs_text_list(self):
        breadcrumbs_text = self.wait_elements(self.ALL_BREADCRUMBS_TEXT)
        breadcrumbs_list = [el.text.strip() for el in breadcrumbs_text]

        return breadcrumbs_list

    @property
    def subcategories_header(self):
        subcategories = self.wait_element(self.SUBCATEGORIES_HEADER)

        return subcategories

    @property
    def all_subcategories_list(self):
        all_subcategories = self.wait_elements(self.ALL_SUBCATEGORIES)
        list_subcategories = [el.text.strip() for el in all_subcategories]

        return list_subcategories

    def click_to_men_categories_button(self):
        button = self.wait_element(self.MEN_CATEGORIES_BUTTON)
        button.click()

    def click_to_women_categories_link(self):
        link = self.wait_element(self.WOMEN_CATEGORIES_LINK)
        link.click()
