import pytest
import time

from fixtures.driver import driver
from fixtures.url import presta_shop_url
from utils.click_to_random_products_card import click_to_random_elements
from utils.wait_element import wait_element, wait_elements

@pytest.mark.product_card
def test_check_breadcrumb_with_header(driver, presta_shop_url):
    driver.get(presta_shop_url)
    click_to_random_elements(driver, wait_elements, ".thumbnail.product-thumbnail")

    pass

def test_coast_is_display():
    pass

def test_add_to_cart_is_display():
    pass

def test_click_to_add_to_cart():
    pass

def test_share_to_facebook_is_display():
    pass

def test_share_to_x_is_display():
    pass

def test_share_to_pinterest_is_display():
    pass

def test_add_in_wishlist_is_display():
    pass

def test_click_to_add_in_wishlist(driver, presta_shop_url):
    pass


