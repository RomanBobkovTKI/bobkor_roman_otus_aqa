import pytest
from fixtures.driver import driver
from fixtures.url import presta_shop_url
from utils.add_new_product import add_new_product
from utils.login_to_admin import login_to_admin


@pytest.fixture
def admin_login(driver, presta_shop_url):
    login_to_admin(driver, presta_shop_url)
    return driver

@pytest.fixture
def product_admin_driver(driver, presta_shop_url):
    login_to_admin(driver, presta_shop_url)
    add_new_product(driver)
    return driver


