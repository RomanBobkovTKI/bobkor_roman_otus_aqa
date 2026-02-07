import pytest

from fixtures.driver import driver
from fixtures.url import presta_shop_url
from utils.wait_element import wait_element


# Знаю что title есть не только на главной странице, но это был "первый тест", решил оставить его тут
@pytest.mark.main_page
def test_title_page(driver, presta_shop_url):
    driver.get(presta_shop_url)
    assert driver.title == "PrestaShop"


@pytest.mark.main_page
def test_contact_us_link(driver, presta_shop_url):
    driver.get(presta_shop_url)

    link = wait_element("#contact-link a", driver)
    link_href = link.get_attribute("href")

    assert "/contact-us" in link_href, (
        f"Неверная ссылка: ожидалось /contact-us, получено {link_href}"
    )


@pytest.mark.main_page
def test_contact_us_click(driver, presta_shop_url):
    driver.get(presta_shop_url)

    link = wait_element("#contact-link a", driver)

    link.click()
    wait_element(".form-fields h3", driver)
    current_url = driver.current_url

    assert "/contact-us" in current_url, (
        f"Неверный роут по переходу 'contact_us': ожидалось /contact-us, получено {current_url}"
    )


@pytest.mark.main_page
def test_search_widget_is_visible(driver, presta_shop_url):
    driver.get(presta_shop_url)

    widget = wait_element("#search_widget", driver)
    assert widget.is_displayed()


@pytest.mark.main_page
def test_placeholder_from_search_widget(driver, presta_shop_url):
    driver.get(presta_shop_url)

    widget = wait_element(
        "#search_widget input[placeholder='Search our catalog']", driver
    )
    placeholder = widget.get_attribute("placeholder")

    assert placeholder == "Search our catalog", (
        f"Неверный placeholder у поискового виджета: ожидалось 'Search our catalog', получено {placeholder}"
    )


@pytest.mark.main_page
def test_sign_in_button_is_visible(driver, presta_shop_url):
    driver.get(presta_shop_url)

    element = wait_element("#_desktop_user_info span", driver)
    text_element = element.text

    assert text_element == "Sign in", (
        f"Неверный текст у кнопки входа: ожидалось 'Sign in', получено {text_element}"
    )
    assert element.is_displayed(), f"Кнопка логина не отображается"


@pytest.mark.main_page
def test_click_to_sign_in_button(driver, presta_shop_url):
    driver.get(presta_shop_url)

    element = wait_element("#_desktop_user_info a", driver)
    element.click()

    header_text = wait_element(".page-header h1", driver).text

    assert header_text == "Log in to your account", (
        f"Неверный текст заголовка: ожидалось 'Log in to your account', получено: {header_text}"
    )
    assert "login" in driver.current_url, (
        f"Неверный роут при переходе на страницу логина, ожидалось: {'/login'}, получено {driver.current_url}"
    )


@pytest.mark.main_page
def test_cart_is_visible(driver, presta_shop_url):
    driver.get(presta_shop_url)

    element = wait_element("#_desktop_cart", driver)

    assert element.is_displayed(), f"Элемент корзины не виден в хедере"


@pytest.mark.main_page
def test_main_logo_is_visible(driver, presta_shop_url):
    driver.get(presta_shop_url)

    logo = wait_element("#_desktop_logo", driver)

    assert logo.is_displayed(), f"Логотип не отображается"


@pytest.mark.main_page
def test_href_main_logo(driver, presta_shop_url):
    driver.get(presta_shop_url)

    logo = wait_element("#_desktop_logo a", driver)
    logo_href = logo.get_attribute("href")

    assert logo_href == f"{presta_shop_url}/", f"Неверный аттрибут href: ожидалось: {"/"}, получено {logo_href}"


@pytest.mark.main_page
def test_click_main_logo(driver, presta_shop_url):
    driver.get(presta_shop_url)

    logo = wait_element("#_desktop_logo a", driver)
    logo.click()

    wait_element("#_desktop_logo a", driver)

    assert driver.current_url == f"{presta_shop_url}/", f"Неверная ссылка по лого"


@pytest.mark.main_page
def test_click_to_clothes_button(driver, presta_shop_url):
    driver.get(presta_shop_url)

    button = wait_element("#category-3", driver)
    button.click()

    header_text = wait_element("h1", driver).text

    assert header_text == "CLOTHES", f"Неверный header страницы, ожидалось: {"CLOTHES"}, получено {header_text}"
    assert "clothes" in driver.current_url, f"Неверный url по переходу в clothes, ожидалсь совпадение по {"clothes"}, получено {driver.current_url}"


@pytest.mark.main_page
def test_click_to_accessories_button(driver, presta_shop_url):
    driver.get(presta_shop_url)

    button = wait_element("#category-6", driver)
    button.click()

    header_text = wait_element("h1", driver).text

    assert header_text == "ACCESSORIES", f"Неверный header страницы, ожидалось: {"ACCESSORIES"}, получено {header_text}"
    assert "accessories" in driver.current_url, f"Неверный url по переходу в accessories, ожидалсь совпадение по {"accessories"}, получено {driver.current_url}"