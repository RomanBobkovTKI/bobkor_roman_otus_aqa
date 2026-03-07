import pytest
import allure

from fixtures.driver import driver
from page_object_model.elements.header import Header
from page_object_model.elements.sign_in_login_modal import SignInLoginModal
from page_object_model.elements.success_add_to_cart_modal import SuccessAddToCartModal
from page_object_model.main_page import MainPage
from page_object_model.product_card_page import ProductCard
from utils.asserts.assert_text_equals import assert_element_text_equals


@allure.feature("Карточка товара")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Тесты на странице с карточкой товара")
@pytest.mark.product_card
class TestProductCard:
    @allure.title("Проверка названия в хлебных крошках")
    def test_check_breadcrumb_with_header(self, driver):
        MainPage(driver).click_to_random_product_card()
        breadcrumbs_text = (
            ProductCard(driver).product_name_from_breadcrumbs.text.strip().lower()
        )
        header_card_text = ProductCard(driver).header_card_name.text.strip().lower()

        assert breadcrumbs_text == header_card_text, (
            f"Название в крошках {breadcrumbs_text} не совпадает с заголовком карточки товара {header_card_text}"
        )

    @allure.title("Проверка отображение цены")
    def test_coast_is_display(self, driver):
        MainPage(driver).click_to_random_product_card()
        price = ProductCard(driver).price

        assert price.is_displayed(), f"Не отображается цена в карточке товара"

    @allure.title("Проверка отображения кнопки добавления в корзину")
    def test_add_to_cart_is_display(self, driver):
        expected_text = "\ue547 add to cart"
        MainPage(driver).click_to_random_product_card()

        assert_element_text_equals(
            ProductCard(driver).add_to_cart_button.text, expected_text
        )
        assert ProductCard(driver).add_to_cart_button, (
            f"Кнопка добавления в корзину не отображается"
        )

    @allure.title("Добавление в корзину")
    def test_click_to_add_to_cart(self, driver):
        product_count_before = Header(driver).count_item_in_cart
        MainPage(driver).click_to_random_product_card()
        ProductCard(driver).click_to_add_to_cart()
        SuccessAddToCartModal(driver).click_to_close_modal()
        product_count_after = Header(driver).count_item_in_cart

        assert product_count_before < product_count_after, (
            f"Счетчик в корзине не увеличился после добавлению товара в корзину, ожидаем что стало: {product_count_before}, до добавления было: {product_count_after}"
        )

    @allure.title("Проверка отображения кнопки поделиться в фейсбук")
    def test_share_to_facebook_is_display(self, driver):
        MainPage(driver).click_to_random_product_card()

        assert ProductCard(driver).facebook_icon.is_displayed(), (
            f"Не отображается иконка фейсбука в share блоке"
        )

    @allure.title("Проверка отображения кнопки поделиться в Х")
    def test_share_to_x_is_display(self, driver):
        MainPage(driver).click_to_random_product_card()

        assert ProductCard(driver).x_icon.is_displayed(), (
            f"Не отобрадается иконка twitter(x) в share блоке"
        )

    @allure.title("Проверка отображения кнопки поделиться в пинтерест")
    def test_share_to_pinterest_is_display(self, driver):
        MainPage(driver).click_to_random_product_card()

        assert ProductCard(driver).pinterest_icon.is_displayed(), (
            f"Не отображается иконка пинтерест в share блоке"
        )

    @allure.title("Проверка отображения кнопки добавления в избранное")
    def test_add_in_wishlist_is_display(self, driver):
        MainPage(driver).click_to_random_product_card()

        assert ProductCard(driver).wishlist_button.is_displayed(), (
            f"Не отображается кнопка добавления в виш-лист"
        )

    @allure.title("[Пользователь не авторизован] Нажатие на добавление в избранное")
    def test_click_to_add_in_wishlist_no_auth(self, driver):
        MainPage(driver).click_to_random_product_card()
        ProductCard(driver).click_to_add_to_wishlist()

        assert SignInLoginModal(driver).header.is_displayed(), (
            f"Не отображается хедер в модальном окне"
        )
