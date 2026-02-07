import pytest
from selenium.webdriver.common.by import By

from fixtures.driver import driver
from fixtures.url import presta_shop_url
from utils.wait_element import wait_element, wait_elements

@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", ["3-clothes"], indirect=True)
def test_clothes_page(driver, presta_shop_url):
    driver.get(presta_shop_url)

    header = wait_element("h1", driver)
    header_text = header.text

    assert "CLOTHES" in header_text, f"Неверный header, ожидалось {"CLOTHES"}, получили {header_text.text}"
    assert header.is_displayed(), f"Не отображается header"


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", ["3-clothes"], indirect=True)
def test_breadcrumbs(driver, presta_shop_url):
    driver.get(presta_shop_url)

    breadcrumbs = wait_elements(".breadcrumb span", driver)
    actual_texts = [el.text.strip() for el in breadcrumbs]
    expected_texts = ["Home", "Clothes"]

    assert actual_texts == expected_texts, f"Неверные элементы в хлебных крошках, ожидалось {expected_texts}, получили {actual_texts}"


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", ["3-clothes"], indirect=True)
def test_subcategories(driver, presta_shop_url):
    driver.get(presta_shop_url)

    subcategories = wait_element(".subcategory-heading", driver)
    subcategories_text = subcategories.text

    assert "Subcategories" == subcategories_text, f"Неверный текст у Subcategories"
    assert subcategories.is_displayed(), f"Хедер Subcategories не отображается"


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", ["3-clothes"], indirect=True)
def test_subcategories_clothes(driver, presta_shop_url):
    driver.get(presta_shop_url)

    subcategories = wait_elements(".subcategory-name", driver)
    actual_texts = [el.text.strip() for el in subcategories]
    expected_texts = ["MEN", "WOMEN"]

    assert expected_texts == actual_texts


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", ["3-clothes"], indirect=True)
def test_click_on_men_categories(driver, presta_shop_url):
    driver.get(presta_shop_url)

    button = wait_element("//div[contains(@class, 'subcategory-image')]//a[contains(@href, '4-men')]", driver, by=By.XPATH)
    button.click()

    header = wait_element("h1", driver)
    header_text = header.text

    assert "MEN" == header_text, f"Неверный заголовок страницы, ожидалось: MEN, получили {header_text}"
    assert "4-men" in driver.current_url, f"Неверный url после перехода, ожидалось содержание 4-men, получили {driver.current_url}"


@pytest.mark.clothes_page
@pytest.mark.parametrize("presta_shop_url", ["3-clothes"], indirect=True)
def test_click_on_women_categories(driver, presta_shop_url):
    driver.get(presta_shop_url)

    button = wait_element("a[title='Women']", driver)
    button.click()

    header = wait_element("h1", driver)
    header_text = header.text

    assert "WOMEN" == header_text, f"Неверный заголовок страницы, ожидалось: WOMEN, получиди {header_text}"
    assert "5-women" in driver.current_url, f"Неверный url после перехода, ожидалось содержание 5-women, получили {driver.current_url}"