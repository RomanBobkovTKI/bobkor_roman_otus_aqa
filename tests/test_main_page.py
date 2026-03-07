import pytest
import allure
from fixtures.driver import driver
from fixtures.url import presta_shop_url
from page_object_model.accessories_page import AccessoriesPage
from page_object_model.base_page import BasePage
from page_object_model.clothes_page import ClothesPage
from page_object_model.contact_us_page import ContactUs
from page_object_model.elements.header import Header
from page_object_model.login_page import LoginPage
from page_object_model.main_page import MainPage
from utils.asserts.assert_text_equals import assert_element_text_equals
from utils.currency_symbol import extract_currency_symbol


@allure.feature("Главная страница")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Тесты на главной странице")
@pytest.mark.main_page
class TestMainPage:
    # Знаю что title есть не только на главной странице, но это был "первый тест", решил оставить его тут
    @allure.title("Проверка title в <head> теге")
    def test_title_page(self, driver):
        expected_title = "PrestaShop"
        actual_title = BasePage(driver).title

        assert expected_title == actual_title

    @allure.title("Проверка ссылки в тексте 'Contact-us'")
    def test_contact_us_link(self, driver):
        expected_link = "/contact-us"
        actual_link = Header(driver).contact_us_link

        assert expected_link in actual_link, (
            f"Неверная ссылка: ожидалось /contact-us, получено {actual_link}"
        )

    @allure.title("Успешный переход на /contact-us")
    def test_contact_us_click(self, driver):
        expected_link = "/contact-us"

        Header(driver).click_contact_us_link()
        ContactUs(driver).header_page_text

        assert expected_link in BasePage(driver).current_url, (
            f"Неверный роут по переходу 'contact_us': ожидалось /contact-us, получено {BasePage(driver).current_url}"
        )

    @allure.title("Виджет поиска отображается на странице")
    def test_search_widget_is_visible(self, driver):
        widget = Header(driver).widget_input_element
        assert widget.is_displayed()

    @allure.title("Проверка плейсхолдера в инпуте поиска")
    def test_placeholder_from_search_widget(self, driver):
        expected_placeholder = "Search our catalog"
        actual_placeholder = Header(driver).widget_input_placeholder

        assert expected_placeholder == actual_placeholder, (
            f"Неверный placeholder у поискового виджета: ожидалось {expected_placeholder}, получено {actual_placeholder}"
        )

    @allure.title("Кнопка 'Sign In' отображается на странице")
    def test_sign_in_button_is_visible(self, driver):
        expected_text = "sign in"
        sign_in_button = Header(driver).sign_in_button
        sign_in_text = sign_in_button.text.lower()

        assert_element_text_equals(sign_in_text, expected_text)
        assert sign_in_button.is_displayed(), f"Кнопка логина не отображается"

    @allure.title("Успешный переход на страницу логина /login")
    def test_click_to_sign_in_button(self, driver):
        expected_header_text = "Log in to your account".lower()
        expected_url = "login"
        Header(driver).click_to_sign_in_link()

        assert_element_text_equals(
            LoginPage(driver).header_element.text, expected_header_text
        )
        assert expected_url in BasePage(driver).current_url, (
            f"Неверный роут при переходе на страницу логина, ожидалось: {expected_url}, получено {BasePage(driver).current_url}"
        )

    @allure.title("Отображение корзины в хедере страницы")
    def test_cart_is_visible(self, driver):
        cart = Header(driver).cart_element

        assert cart.is_displayed(), f"Элемент корзины не виден в хедере"

    @allure.title("Лого отображается на странице")
    def test_main_logo_is_visible(self, driver):
        logo = Header(driver).logo_element

        assert logo.is_displayed(), f"Логотип не отображается"

    @allure.title("Проверка ссылки в лого в хедере")
    def test_href_main_logo(self, driver, presta_shop_url):
        expected_url = f"{presta_shop_url}/"
        logo_href = Header(driver).logo_link_element.get_attribute("href")

        assert logo_href == expected_url, (
            f"Неверный аттрибут href: ожидалось: {expected_url}, получено {logo_href}"
        )

    @allure.title("Успешный клик на лого и переход на главную страницу")
    def test_click_main_logo(self, driver, presta_shop_url):
        expected_url = f"{presta_shop_url}/"
        Header(driver).click_to_logo()
        Header(driver).logo_link_element

        assert BasePage(driver).current_url == expected_url, f"Неверная ссылка по лого"

    @allure.title("Успешный переход на страницу категорий /clothes")
    def test_click_to_clothes_button(self, driver):
        expected_header_text = "clothes"
        expected_url_path = "clothes"
        Header(driver).click_to_clothes_button()

        assert_element_text_equals(
            ClothesPage(driver).header.text, expected_header_text
        )
        assert expected_url_path in BasePage(driver).current_url, (
            f"Неверный url по переходу в clothes, ожидалсь совпадение по {expected_url_path}, получено {BasePage(driver).current_url}"
        )

    @allure.title("Успешный переход на страницу с аксессуарами /accessories")
    def test_click_to_accessories_button(self, driver):
        expected_header_text = "accessories"
        expected_url_path = "accessories"
        Header(driver).click_to_accessories_button()

        assert_element_text_equals(
            AccessoriesPage(driver).header.text, expected_header_text
        )
        assert expected_url_path in BasePage(driver).current_url, (
            f"Неверный url по переходу в accessories, ожидалсь совпадение по {expected_url_path}, получено {BasePage(driver).current_url}"
        )

    @allure.title("Смена валюты через currency в хедере")
    def test_change_currency(self, driver, presta_shop_url):
        expected_dollar_query = "?SubmitCurrency=1&id_currency=2"

        random_price = MainPage(driver).currency_price_element.text
        currency_symbol_before = extract_currency_symbol(random_price)

        Header(driver).click_to_change_currency_button()
        Header(driver).click_to_dollar_value_in_currency_option()

        random_price = MainPage(driver).currency_price_element.text
        currency_symbol_after = extract_currency_symbol(random_price)

        assert currency_symbol_before != currency_symbol_after
        assert expected_dollar_query in BasePage(driver).current_url
