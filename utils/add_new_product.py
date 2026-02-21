from page_object_model.administration_main_page import AdministrationMainPage
from page_object_model.administration_products_page import AdministrationProductsPage
from utils.product import get_random_product


def add_new_product(driver):
    admin_main_page = AdministrationMainPage(driver)
    admin_product_page = AdministrationProductsPage(driver)
    product = get_random_product()

    admin_main_page.click_to_subtab_admin_catalog()
    admin_main_page.click_to_subtab_admin_products()
    admin_product_page.click_add_new_product()
    admin_product_page.click_add_new_product_in_modal()

    admin_product_page.clear_product_name()

    admin_product_page.send_keys_to_product_name(
        product["product_name"]
    )

    admin_product_page.click_to_save_product_button()