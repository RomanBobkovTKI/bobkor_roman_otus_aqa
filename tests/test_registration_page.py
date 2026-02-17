import pytest

from fixtures.driver import driver
from page_object_model.base_page import BasePage
from page_object_model.login_page import LoginPage
from page_object_model.main_page import MainPage
from page_object_model.registration_page import RegistrationPage
from utils.user import get_random_user


@pytest.mark.registration_page
@pytest.mark.parametrize("presta_shop_url", [RegistrationPage.URL], indirect=True)
def test_header_is_displayed(driver):
    expected_header_text = "create an account"
    actual_header_text = RegistrationPage(driver).header.text.strip().lower()

    assert actual_header_text == expected_header_text, (
        f"Не совпадает заголовок страницы регистрации, ожидалось {expected_header_text}, получили {actual_header_text}"
    )
    assert RegistrationPage(driver).header.is_displayed(), (
        f"Не отображается хедер на странице регистрации"
    )


@pytest.mark.registration_page
@pytest.mark.parametrize("presta_shop_url", [RegistrationPage.URL], indirect=True)
def test_have_account_click(driver):
    expected_header_text = "log in to your account"
    expected_url_path = "login"
    RegistrationPage(driver).click_to_log_in_instead()
    login_header_text = LoginPage(driver).header_element.text.strip().lower()

    assert login_header_text == expected_header_text, (
        f"Неверный заголовок на странице авторизации, ожиадли {expected_header_text}, получаем {login_header_text}"
    )
    assert expected_url_path in BasePage(driver).current_url


@pytest.mark.registration_page
@pytest.mark.parametrize("presta_shop_url", [RegistrationPage.URL], indirect=True)
def test_click_in_save_button(driver):
    initial_url = BasePage(driver).current_url
    RegistrationPage(driver).clear_first_name_input()
    RegistrationPage(driver).click_to_save_button()

    assert BasePage(driver).current_url == initial_url

    # Вот этот тест помогла мне написать нейронная сеть, это норма практика?
    assert driver.execute_script(
        "return !arguments[0].validity.valid;",
        RegistrationPage(driver).first_name_input,
    )
    assert driver.execute_script(
        "return arguments[0].validity.valueMissing;",
        RegistrationPage(driver).first_name_input,
    )


@pytest.mark.registration_page
@pytest.mark.parametrize("presta_shop_url", [RegistrationPage.URL], indirect=True)
def test_register_user(driver):
    user = get_random_user()
    expected_full_name = f"{user['first_name']} {user['last_name']}"

    RegistrationPage(driver).clear_first_name_input()
    RegistrationPage(driver).clear_last_name_input()
    RegistrationPage(driver).clear_email_input()
    RegistrationPage(driver).clear_password_input()
    RegistrationPage(driver).clear_birthday_input()
    RegistrationPage(driver).send_keys_to_first_name_input(user["first_name"])
    RegistrationPage(driver).send_keys_to_last_name_input(user["last_name"])
    RegistrationPage(driver).send_keys_to_email_input(user["email"])
    RegistrationPage(driver).send_keys_to_password_input(user["password"])
    RegistrationPage(driver).send_keys_to_birthday_input(user["birth_date"])
    RegistrationPage(driver).click_to_checkbox_privacy_input()
    RegistrationPage(driver).click_to_checkbox_privacy_data_input()
    RegistrationPage(driver).click_to_save_button()

    full_name = MainPage(driver).user_full_name.text

    assert full_name == expected_full_name, f"Регистрация завершилась неудачно"


@pytest.mark.registration_page
@pytest.mark.parametrize("presta_shop_url", [RegistrationPage.URL], indirect=True)
def test_password_is_not_visible(driver):
    expected_type = "password"
    type_input = RegistrationPage(driver).password_input.get_attribute("type")

    assert type_input == expected_type, (
        f"Неверный тип инпута, ожидалось: {expected_type}, получили {type_input}"
    )
