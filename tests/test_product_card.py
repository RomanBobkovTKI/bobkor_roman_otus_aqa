import pytest

from fixtures.driver import driver
from page_object_model.elements.header import Header
from page_object_model.elements.sign_in_login_modal import SignInLoginModal
from page_object_model.elements.success_add_to_cart_modal import SuccessAddToCartModal
from page_object_model.main_page import MainPage
from page_object_model.product_card_page import ProductCard


@pytest.mark.product_card
def test_check_breadcrumb_with_header(driver):
    MainPage(driver).click_to_random_product_card()
    breadcrumbs_text = (
        ProductCard(driver).product_name_from_breadcrumbs.text.strip().lower()
    )
    header_card_text = ProductCard(driver).header_card_name.text.strip().lower()

    assert breadcrumbs_text == header_card_text, (
        f"Название в крошках {breadcrumbs_text} не совпадает с заголовком карточки товара {header_card_text}"
    )


@pytest.mark.product_card
def test_coast_is_display(driver):
    MainPage(driver).click_to_random_product_card()
    price = ProductCard(driver).price

    assert price.is_displayed(), f"Не отображается цена в карточке товара"


@pytest.mark.product_card
def test_add_to_cart_is_display(driver):
    expected_text = "\ue547 add to cart"
    MainPage(driver).click_to_random_product_card()
    actual_button_text = ProductCard(driver).add_to_cart_button.text.strip().lower()

    assert actual_button_text == expected_text, (
        f"Неверная надпись на кнопке добавления в корзину, ожиадлось: {expected_text}, получили: {actual_button_text}"
    )
    assert ProductCard(driver).add_to_cart_button, (
        f"Кнопка добавления в корзину не отображается"
    )


@pytest.mark.product_card
def test_click_to_add_to_cart(driver):
    product_count_before = Header(driver).count_item_in_cart
    MainPage(driver).click_to_random_product_card()
    ProductCard(driver).click_to_add_to_cart()
    SuccessAddToCartModal(driver).click_to_close_modal()
    product_count_after = Header(driver).count_item_in_cart

    assert product_count_before < product_count_after, (
        f"Счетчик в корзине не увеличился после добавлению товара в корзину, ожидаем что стало: {product_count_before}, до добавления было: {product_count_after}"
    )


@pytest.mark.product_card
def test_share_to_facebook_is_display(driver):
    MainPage(driver).click_to_random_product_card()

    assert ProductCard(driver).facebook_icon.is_displayed(), (
        f"Не отображается иконка фейсбука в share блоке"
    )


@pytest.mark.product_card
def test_share_to_x_is_display(driver):
    MainPage(driver).click_to_random_product_card()

    assert ProductCard(driver).x_icon.is_displayed(), (
        f"Не отобрадается иконка twitter(x) в share блоке"
    )


@pytest.mark.product_card
def test_share_to_pinterest_is_display(driver):
    MainPage(driver).click_to_random_product_card()

    assert ProductCard(driver).pinterest_icon.is_displayed(), (
        f"Не отображается иконка пинтерест в share блоке"
    )


@pytest.mark.product_card
def test_add_in_wishlist_is_display(driver):
    MainPage(driver).click_to_random_product_card()

    assert ProductCard(driver).wishlist_button.is_displayed(), (
        f"Не отображается кнопка добавления в виш-лист"
    )


@pytest.mark.product_card
def test_click_to_add_in_wishlist_no_auth(driver):
    MainPage(driver).click_to_random_product_card()
    ProductCard(driver).click_to_add_to_wishlist()

    assert SignInLoginModal(driver).header.is_displayed(), (
        f"Не отображается хедер в модальном окне"
    )
