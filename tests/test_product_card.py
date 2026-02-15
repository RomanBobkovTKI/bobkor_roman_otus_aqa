import re
import time

import pytest

from selenium.webdriver.common.by import By

from fixtures.driver import driver
from fixtures.url import presta_shop_url
from utils.click_to_random_products_card import click_to_random_elements
from utils.wait_element import wait_element, wait_elements


@pytest.mark.product_card
def test_check_breadcrumb_with_header(driver, presta_shop_url):
    driver.get(presta_shop_url)
    click_to_random_elements(driver, wait_elements, ".thumbnail.product-thumbnail")

    breadcrumbs_text = wait_element(".breadcrumb ol li:last-child", driver).text
    header_card_text = wait_element("h1", driver).text

    assert breadcrumbs_text.strip().lower() == header_card_text.strip().lower(), (
        f"Название в крошках {breadcrumbs_text} не совпадает с заголовком карточки товара {header_card_text}"
    )


@pytest.mark.product_card
def test_coast_is_display(driver, presta_shop_url):
    driver.get(presta_shop_url)
    click_to_random_elements(driver, wait_elements, ".thumbnail.product-thumbnail")

    price = wait_element(".current-price-value", driver)

    assert price.is_displayed(), f"Не отображается цена в карточке товара"


@pytest.mark.product_card
def test_add_to_cart_is_display(driver, presta_shop_url):
    driver.get(presta_shop_url)
    click_to_random_elements(driver, wait_elements, ".thumbnail.product-thumbnail")

    button = wait_element(".add-to-cart", driver)
    button_text = button.text.strip()

    assert button_text.lower() == "\ue547 add to cart", (
        f"Неверная надпись на кнопке добавления в корзину, ожиадлось: {'\ue547 add to cart'}, получили: {button_text}"
    )
    assert button.is_displayed(), f"Кнопка добавления в корзину не отображается"


@pytest.mark.product_card
def test_click_to_add_to_cart(driver, presta_shop_url):
    driver.get(presta_shop_url)
    products_count_str = wait_element(".cart-products-count", driver).text
    product_count_before = int(re.search(r"\d+", products_count_str).group())
    click_to_random_elements(driver, wait_elements, ".thumbnail.product-thumbnail")

    button = wait_element(".add-to-cart", driver)
    button.click()

    wait_element(".modal-header .close .material-icons", driver).click()

    products_count_str = wait_element(".cart-products-count", driver).text
    product_count_after = int(re.search(r"\d+", products_count_str).group())

    print(product_count_before, product_count_after)
    assert product_count_before < product_count_after


@pytest.mark.product_card
def test_share_to_facebook_is_display(driver, presta_shop_url):
    driver.get(presta_shop_url)
    click_to_random_elements(driver, wait_elements, ".thumbnail.product-thumbnail")

    fb_icon = wait_element(".facebook.icon-gray", driver)

    assert fb_icon.is_displayed(), f"Не отображается иконка фейсбука в share блоке"


@pytest.mark.product_card
def test_share_to_x_is_display(driver, presta_shop_url):
    driver.get(presta_shop_url)
    click_to_random_elements(driver, wait_elements, ".thumbnail.product-thumbnail")

    x_icon = wait_element(".twitter.icon-gray", driver)

    assert x_icon.is_displayed(), f"Не отобрадается иконка twitter(x) в share блоке"


@pytest.mark.product_card
def test_share_to_pinterest_is_display(driver, presta_shop_url):
    driver.get(presta_shop_url)
    click_to_random_elements(driver, wait_elements, ".thumbnail.product-thumbnail")

    pin_icon = wait_element(".pinterest.icon-gray", driver)

    assert pin_icon.is_displayed(), f"Не отображается иконка пинтерест в share блоке"


@pytest.mark.product_card
def test_add_in_wishlist_is_display(driver, presta_shop_url):
    driver.get(presta_shop_url)
    click_to_random_elements(driver, wait_elements, ".thumbnail.product-thumbnail")

    add_to_wishlist_button = wait_element(
        ".wishlist-button-add.wishlist-button-product", driver
    )

    assert add_to_wishlist_button.is_displayed(), (
        f"Не отображается кнопка добавления в виш-лист"
    )


@pytest.mark.product_card
def test_click_to_add_in_wishlist_no_auth(driver, presta_shop_url):
    driver.get(presta_shop_url)
    click_to_random_elements(driver, wait_elements, ".thumbnail.product-thumbnail")

    add_to_wishlist_button = wait_element(
        ".wishlist-button-add.wishlist-button-product", driver
    )
    add_to_wishlist_button.click()

    sign_in_header_modal = wait_element(
        "//h5[@class='modal-title' and text()='Sign in']", driver, by=By.XPATH
    )

    assert sign_in_header_modal.is_displayed(), (
        f"Не отображается хедер в модальном окне"
    )
