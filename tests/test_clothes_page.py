import pytest

from fixtures.driver import driver
from fixtures.url import presta_shop_url
from page_object_model.base_page import BasePage
from page_object_model.clothes_page import ClothesPage
from page_object_model.elements.header import Header
from page_object_model.main_page import MainPage
from page_object_model.men_categories_page import MenCategories
from page_object_model.women_categories_page import WomenCategories
from utils.asserts.assert_text_equals import assert_element_text_equals
from utils.currency_symbol import extract_currency_symbol


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", [ClothesPage.URL], indirect=True)
def test_clothes_page(driver):
    expected_header_text = "clothes"

    assert_element_text_equals(ClothesPage(driver).header.text, expected_header_text)
    assert ClothesPage(driver).header.is_displayed(), f"Не отображается header"


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", [ClothesPage.URL], indirect=True)
def test_breadcrumbs(driver):
    expected_texts = ["Home", "Clothes"]
    actual_texts = ClothesPage(driver).breadcrumbs_text_list

    assert actual_texts == expected_texts, (
        f"Неверные элементы в хлебных крошках, ожидалось {expected_texts}, получили {actual_texts}"
    )


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", [ClothesPage.URL], indirect=True)
def test_subcategories(driver):
    expected_header_text = "subcategories"

    assert_element_text_equals(
        ClothesPage(driver).subcategories_header.text, expected_header_text
    )
    assert ClothesPage(driver).subcategories_header.is_displayed(), (
        f"Хедер Subcategories не отображается"
    )


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", [ClothesPage.URL], indirect=True)
def test_subcategories_clothes(driver):
    expected_texts = ["MEN", "WOMEN"]
    actual_texts = ClothesPage(driver).all_subcategories_list

    assert expected_texts == actual_texts, (
        f"Некорректные сабкатегории, ожидалось: {expected_texts}, получили {actual_texts}"
    )


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", [ClothesPage.URL], indirect=True)
def test_click_on_men_categories(driver):
    expected_header_text = "men"
    expected_men_url = "4-men"
    ClothesPage(driver).click_to_men_categories_button()

    assert_element_text_equals(MenCategories(driver).header.text, expected_header_text)
    assert expected_men_url in BasePage(driver).current_url, (
        f"Неверный url после перехода, ожидалось содержание {expected_men_url}, получили {BasePage(driver).current_url}"
    )


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", [ClothesPage.URL], indirect=True)
def test_click_on_women_categories(driver):
    expected_header_text = "women"
    expected_women_url = "5-women"
    ClothesPage(driver).click_to_women_categories_link()

    assert_element_text_equals(
        WomenCategories(driver).header.text, expected_header_text
    )
    assert expected_women_url in BasePage(driver).current_url, (
        f"Неверный url после перехода, ожидалось содержание 5-women, получили {BasePage(driver).current_url}"
    )


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", [ClothesPage.URL], indirect=True)
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
