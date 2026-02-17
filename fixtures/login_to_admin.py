import pytest
from fixtures.driver import driver
from fixtures.url import presta_shop_url
from page_object_model.administration_main_page import AdministrationMainPage
from page_object_model.administration_products_page import AdministrationProductsPage
from utils.product import get_random_product
from utils.wait_element import wait_element


def login_to_admin(driver, base_url):
    admin_url = f"{base_url.rstrip('/')}/administration/login?_token="  # или как у вас называется папка
    driver.get(admin_url)

    email_input = wait_element("#email", driver)
    password_input = wait_element("#passwd", driver)
    login_button = wait_element("#submit_login", driver)

    email_input.clear()
    password_input.clear()

    # вот тут наверно нужен какой-то дата сет с тестовыми данными
    email_input.send_keys("admin@example.com")
    password_input.send_keys("Admin123!")

    login_button.click()

    wait_element("h1.page-title", driver, timeout=10)

def add_new_product(driver):
    product = get_random_product()

    AdministrationMainPage(driver).click_to_subtab_admin_catalog()
    AdministrationMainPage(driver).click_to_subtab_admin_products()
    AdministrationProductsPage(driver).click_add_new_product()
    AdministrationProductsPage(driver).click_add_new_product_in_modal()

    AdministrationProductsPage(driver).clear_product_name()

    AdministrationProductsPage(driver).send_keys_to_product_name(
        product["product_name"]
    )

    AdministrationProductsPage(driver).click_to_save_product_button()

@pytest.fixture
def admin_login(driver, presta_shop_url):
    login_to_admin(driver, presta_shop_url)
    yield driver

@pytest.fixture
def add_product_driver(admin_login):
    add_new_product(admin_login)
    yield admin_login


