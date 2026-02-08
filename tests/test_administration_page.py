import pytest

from fixtures.driver import driver
from fixtures.url import presta_shop_url
from utils.wait_element import wait_element

@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", ["administration/login?_token="], indirect=True)
def test_email_input_is_desplayed(driver, presta_shop_url):
    driver.get(presta_shop_url)

    email_input = wait_element("#email", driver)
    mail_label_text = wait_element("label[for='email']", driver).text.strip().lower()

    assert email_input.is_displayed(), f"Не отображается инпут ввода мейла"
    assert mail_label_text == "email address", f"Не соотвествует лейбл к инпуту, ожидалось: email address, получили: {mail_label_text}"


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", ["administration/login?_token="], indirect=True)
def test_password_input_is_desplayed(driver, presta_shop_url):
    driver.get(presta_shop_url)

    password_input = wait_element("#passwd", driver)
    password_label_text = wait_element("label[for='passwd']", driver).text.strip().lower()

    assert password_input.is_displayed(), f"Не отображается инпут ввода пароля"
    assert password_label_text == "password", f"Не соотвествует лейбл к инпуту, ожидалось: password, получили: {password_label_text}"


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", ["administration/login?_token="], indirect=True)
def test_login_button_is_desplayed(driver, presta_shop_url):
    driver.get(presta_shop_url)

    login_button = wait_element("#submit_login", driver)
    login_button_text = login_button.text.strip().lower()

    assert login_button_text == 'log in', f"Не совпадает текст в кнопке логина, ожидаем: {"log in"}, получаем {login_button_text}"
    assert login_button.is_displayed(), f"Не отображается кнопка логина"


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", ["administration/login?_token="], indirect=True)
def test_click_to_forgot_pass(driver, presta_shop_url):
    driver.get(presta_shop_url)

    forgot_pass_button = wait_element("#forgot-password-link", driver)
    reset_password_button = wait_element("#request_password_reset_buttons_submit_login", driver)
    forgot_pass_button_text = forgot_pass_button.text.strip().lower()

    forgot_pass_button.click()

    assert forgot_pass_button_text == "i forgot my password", f"Не совпадает текст восстановления пароля, ожидаем: {"i forgot my password"}, получаем: {forgot_pass_button_text}"
    assert reset_password_button.is_displayed(), f"Не видна кнопка восстановления пароля"

@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", ["administration/login?_token="], indirect=True)
def test_stay_logged_in(driver, presta_shop_url):
    driver.get(presta_shop_url)

    stay_logged_in = wait_element(".md-checkbox label", driver)
    stay_logged_in_text = stay_logged_in.text.strip().lower()

    assert stay_logged_in_text == "stay logged in", f"Не совпадет текст: {"stay logged in"}, ожидалось: {stay_logged_in_text}"
    assert stay_logged_in.is_displayed(), f"Не отображается надпись {"stay logged in"}"