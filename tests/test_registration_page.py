import pytest
from selenium.webdriver.common.by import By

from fixtures.driver import driver
from fixtures.url import presta_shop_url
from utils.wait_element import wait_element
from utils.user import get_random_user


@pytest.mark.registration_page
@pytest.mark.parametrize("presta_shop_url", ["registration"], indirect=True)
def test_header_is_displayed(driver, presta_shop_url):
    driver.get(presta_shop_url)

    header = wait_element(".page-header h1", driver)
    header_text = header.text.strip().lower()

    assert header_text == "create an account", (
        f"Не совпадает заголовок страницы регистрации, ожидалось {'create an account'}, получили {header_text}"
    )
    assert header.is_displayed(), f"Не отображается хедер на странице регистрации"


@pytest.mark.registration_page
@pytest.mark.parametrize("presta_shop_url", ["registration"], indirect=True)
def test_have_account_click(driver, presta_shop_url):
    driver.get(presta_shop_url)

    have_account_button = wait_element(
        "//section//a[contains(@href, 'login')]", driver, by=By.XPATH
    )
    have_account_button.click()

    log_in_header = wait_element("h1", driver)
    login_header_text = log_in_header.text.strip().lower()

    assert login_header_text == "log in to your account", (
        f"Неверный заголовок на странице авторизации, ожиадли 'Log in to your account', получаем {log_in_header}"
    )
    assert "login" in driver.current_url


@pytest.mark.registration_page
@pytest.mark.parametrize("presta_shop_url", ["registration"], indirect=True)
def test_click_in_save_button(driver, presta_shop_url):
    driver.get(presta_shop_url)

    first_name_input = wait_element("#field-firstname", driver)
    save_button = wait_element(
        "//button[contains(@type, 'submit')]", driver, by=By.XPATH
    )

    first_name_input.clear()

    initial_url = driver.current_url

    save_button.click()

    assert driver.current_url == initial_url

    # Вот этот тест помогла мне написать нейронная сеть, это норма практика?
    assert driver.execute_script(
        "return !arguments[0].validity.valid;", first_name_input
    )
    assert driver.execute_script(
        "return arguments[0].validity.valueMissing;", first_name_input
    )


@pytest.mark.registration_page
@pytest.mark.parametrize("presta_shop_url", ["registration"], indirect=True)
def test_register_user(driver, presta_shop_url):
    user = get_random_user()
    driver.get(presta_shop_url)

    first_name_input = wait_element("#field-firstname", driver)
    last_name_input = wait_element("#field-lastname", driver)
    email_input = wait_element("#field-email", driver)
    password_input = wait_element("#field-password", driver)
    birthday_input = wait_element("#field-birthday", driver)
    checkbox_privacy_input = wait_element("input[name='psgdpr']", driver)
    checkbox_privacy_data = wait_element("input[name = 'customer_privacy']", driver)
    save_button = wait_element(
        "//button[contains(@type, 'submit')]", driver, by=By.XPATH
    )

    first_name_input.clear()
    last_name_input.clear()
    email_input.clear()
    password_input.clear()
    birthday_input.clear()

    first_name_input.send_keys(user["first_name"])
    last_name_input.send_keys(user["last_name"])
    email_input.send_keys(user["email"])
    password_input.send_keys(user["password"])
    birthday_input.send_keys(user["birth_date"])

    checkbox_privacy_input.click()
    checkbox_privacy_data.click()

    save_button.click()

    full_name = wait_element(".account .hidden-sm-down", driver).text

    assert full_name == f"{user['first_name']} {user['last_name']}", (
        f"Регистрация завершилась неудачно"
    )


@pytest.mark.registration_page
@pytest.mark.parametrize("presta_shop_url", ["registration"], indirect=True)
def test_password_is_not_visible(driver, presta_shop_url):
    driver.get(presta_shop_url)

    password_input = wait_element("#field-password", driver)
    type_input = password_input.get_attribute("type")

    assert type_input == "password", (
        f"Неверный тип инпута, ожидалось: passwordб получили {type_input}"
    )
