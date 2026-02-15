import pytest

from fixtures.driver import driver
from fixtures.url import presta_shop_url
from page_object_model.accessories_page import AccessoriesPage
from page_object_model.base_page import BasePage
from page_object_model.clothes_page import ClothesPage
from page_object_model.contact_us_page import ContactUs
from page_object_model.elements.header import Header
from page_object_model.login_page import LoginPage
from page_object_model.main_page import MainPage
from utils.currency_symbol import extract_currency_symbol


# Знаю что title есть не только на главной странице, но это был "первый тест", решил оставить его тут
@pytest.mark.main_page
def test_title_page(driver):
    expected_title = "PrestaShop"
    actual_title = BasePage(driver).title

    assert expected_title == actual_title


@pytest.mark.main_page
def test_contact_us_link(driver):
    expected_link = "/contact-us"
    actual_link = Header(driver).contact_us_link

    assert expected_link in actual_link, (
        f"Неверная ссылка: ожидалось /contact-us, получено {actual_link}"
    )


@pytest.mark.main_page
def test_contact_us_click(driver):
    expected_link = "/contact-us"

    Header(driver).click_contact_us_link()
    ContactUs(driver).header_page_text

    assert expected_link in BasePage(driver).current_url, (
        f"Неверный роут по переходу 'contact_us': ожидалось /contact-us, получено {BasePage(driver).current_url}"
    )


@pytest.mark.main_page
def test_search_widget_is_visible(driver):
    widget = Header(driver).widget_input_element
    assert widget.is_displayed()


@pytest.mark.main_page
def test_placeholder_from_search_widget(driver):
    expected_placeholder = "Search our catalog"
    actual_placeholder = Header(driver).widget_input_placeholder

    assert expected_placeholder == actual_placeholder, (
        f"Неверный placeholder у поискового виджета: ожидалось {expected_placeholder}, получено {actual_placeholder}"
    )


@pytest.mark.main_page
def test_sign_in_button_is_visible(driver):
    expected_text = "Sign In".lower()
    sign_in_button = Header(driver).sign_in_button
    sign_in_text = sign_in_button.text.lower()

    assert expected_text == sign_in_text, (
        f"Неверный текст у кнопки входа: ожидалось {expected_text}, получено {sign_in_text}"
    )
    assert sign_in_button.is_displayed(), f"Кнопка логина не отображается"


@pytest.mark.main_page
def test_click_to_sign_in_button(driver):
    expected_header_text = "Log in to your account".lower()
    expected_url = "login"
    Header(driver).click_to_sign_in_link()
    actual_text = LoginPage(driver).header_element.text.lower()

    assert expected_header_text == actual_text, (
        f"Неверный текст заголовка: ожидалось {expected_header_text}, получено: {actual_text}"
    )
    assert expected_url in BasePage(driver).current_url, (
        f"Неверный роут при переходе на страницу логина, ожидалось: {expected_url}, получено {BasePage(driver).current_url}"
    )


@pytest.mark.main_page
def test_cart_is_visible(driver):
    cart = Header(driver).cart_element

    assert cart.is_displayed(), f"Элемент корзины не виден в хедере"


@pytest.mark.main_page
def test_main_logo_is_visible(driver):
    logo = Header(driver).logo_element

    assert logo.is_displayed(), f"Логотип не отображается"


@pytest.mark.main_page
def test_href_main_logo(driver, presta_shop_url):
    expected_url = f"{presta_shop_url}/"
    logo_href = Header(driver).logo_link_element.get_attribute("href")

    assert logo_href == expected_url, (
        f"Неверный аттрибут href: ожидалось: {expected_url}, получено {logo_href}"
    )


@pytest.mark.main_page
def test_click_main_logo(driver, presta_shop_url):
    expected_url = f"{presta_shop_url}/"
    Header(driver).click_to_logo()
    Header(driver).logo_link_element

    assert BasePage(driver).current_url == expected_url, f"Неверная ссылка по лого"


@pytest.mark.main_page
def test_click_to_clothes_button(driver):
    expected_header_text = "clothes"
    expected_url_path = "clothes"
    Header(driver).click_to_clothes_button()
    header_text = ClothesPage(driver).header.text.strip().lower()

    assert header_text == expected_header_text, (
        f"Неверный header страницы, ожидалось: {expected_header_text}, получено {header_text}"
    )
    assert expected_url_path in BasePage(driver).current_url, (
        f"Неверный url по переходу в clothes, ожидалсь совпадение по {expected_url_path}, получено {BasePage(driver).current_url}"
    )


@pytest.mark.main_page
def test_click_to_accessories_button(driver):
    expected_header_text = "accessories"
    expected_url_path = "accessories"
    Header(driver).click_to_accessories_button()
    actual_header_text = AccessoriesPage(driver).header.text.strip().lower()

    assert expected_header_text == actual_header_text, (
        f"Неверный header страницы, ожидалось: {expected_header_text}, получено {actual_header_text}"
    )
    assert expected_url_path in BasePage(driver).current_url, (
        f"Неверный url по переходу в accessories, ожидалсь совпадение по {expected_url_path}, получено {BasePage(driver).current_url}"
    )


@pytest.mark.main_page
def test_change_currency(driver, presta_shop_url):
    expected_dollar_query = "?SubmitCurrency=1&id_currency=2"

    random_price = MainPage(driver).currency_price_element.text
    currency_symbol_before = extract_currency_symbol(random_price)

    Header(driver).click_to_change_currency_button()
    Header(driver).click_to_dollar_value_in_currency_option()

    random_price = MainPage(driver).currency_price_element.text
    currency_symbol_after = extract_currency_symbol(random_price)

    assert currency_symbol_before != currency_symbol_after
    assert expected_dollar_query in BasePage(driver).current_url
