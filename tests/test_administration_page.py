import pytest

from fixtures.driver import driver
from fixtures.login_to_admin import admin_login, add_product_driver
from page_object_model.administration_login_page import AdministrationPage
from page_object_model.administration_main_page import AdministrationMainPage
from page_object_model.administration_products_page import AdministrationProductsPage
from page_object_model.base_page import BasePage
from utils.product import get_random_product


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_email_input_is_desplayed(driver):
    expected_email_label = "email address"
    actual_mail_label_text = AdministrationPage(driver).email_label.text.strip().lower()

    assert AdministrationPage(driver).email_input.is_displayed(), (
        f"Не отображается инпут ввода мейла"
    )
    assert actual_mail_label_text == expected_email_label, (
        f"Не соотвествует лейбл к инпуту, ожидалось: {expected_email_label}, получили: {actual_mail_label_text}"
    )


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_password_input_is_desplayed(driver):
    expected_password_label = "password"
    actual_password_label_text = (
        AdministrationPage(driver).password_label.text.strip().lower()
    )

    assert AdministrationPage(driver).password_input.is_displayed(), (
        f"Не отображается инпут ввода пароля"
    )
    assert actual_password_label_text == expected_password_label, (
        f"Не соотвествует лейбл к инпуту, ожидалось: {expected_password_label}, получили: {actual_password_label_text}"
    )


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_login_button_is_desplayed(driver):
    expected_login_label = "log in"
    login_button_text = AdministrationPage(driver).login_button.text.strip().lower()

    assert login_button_text == expected_login_label, (
        f"Не совпадает текст в кнопке логина, ожидаем: {expected_login_label}, получаем {login_button_text}"
    )
    assert AdministrationPage(driver).login_button.is_displayed(), (
        f"Не отображается кнопка логина"
    )


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_click_to_forgot_pass(driver):
    expected_forgot_password_text = "i forgot my password"
    forgot_pass_button_text = (
        AdministrationPage(driver).forgot_pass_link.text.strip().lower()
    )
    AdministrationPage(driver).click_to_forgot_pass()

    assert forgot_pass_button_text == expected_forgot_password_text, (
        f"Не совпадает текст восстановления пароля, ожидаем: {expected_forgot_password_text}, получаем: {forgot_pass_button_text}"
    )
    assert AdministrationPage(driver).reset_pass_button.is_displayed(), (
        f"Не видна кнопка восстановления пароля"
    )


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_stay_logged_in(driver):
    expected_text = "stay logged in"
    stay_logged_in_text = (
        AdministrationPage(driver).stay_logged_in_label.text.strip().lower()
    )

    assert stay_logged_in_text == expected_text, (
        f"Не совпадет текст: {expected_text}, ожидалось: {stay_logged_in_text}"
    )
    assert AdministrationPage(driver).stay_logged_in_label.is_displayed(), (
        f"Не отображается надпись {'stay logged in'}"
    )


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_login(driver):
    expected_dashboard_header = "dashboard"
    expected_url_path = "administration/?controller=AdminDashboard"

    AdministrationPage(driver).clear_email_input()
    AdministrationPage(driver).clear_password_input()
    # вот тут наверно нужен какой-то дата сет с тестовыми данными
    AdministrationPage(driver).send_keys_to_email("admin@example.com")
    AdministrationPage(driver).send_keys_to_password("Admin123!")
    AdministrationPage(driver).click_to_log_in_button()

    header_dashboard_text = (
        AdministrationMainPage(driver).dashboard_header.text.strip().lower()
    )

    assert header_dashboard_text == expected_dashboard_header
    assert AdministrationMainPage(driver).dashboard_header.is_displayed()
    assert expected_url_path in BasePage(driver).current_url


@pytest.mark.administration_page
def test_logout(admin_login):
    expected_url_path = "/administration/login"

    AdministrationMainPage(admin_login).click_to_profile_icon()
    AdministrationMainPage(admin_login).click_logout_button()
    AdministrationPage(admin_login).login_logo

    assert expected_url_path in BasePage(admin_login).current_url


@pytest.mark.administration_page
def test_add_new_product(admin_login):
    product = get_random_product()

    AdministrationMainPage(admin_login).click_to_subtab_admin_catalog()
    AdministrationMainPage(admin_login).click_to_subtab_admin_products()
    AdministrationProductsPage(admin_login).click_add_new_product()
    AdministrationProductsPage(admin_login).click_add_new_product_in_modal()

    AdministrationProductsPage(admin_login).clear_product_name()

    AdministrationProductsPage(admin_login).send_keys_to_product_name(
        product["product_name"]
    )

    AdministrationProductsPage(admin_login).click_to_save_product_button()

    assert AdministrationProductsPage(admin_login).success_message.is_displayed(), ()


@pytest.mark.administration_page
def test_delete_product(add_product_driver):
    AdministrationMainPage(add_product_driver).click_to_subtab_admin_catalog()
    AdministrationMainPage(add_product_driver).click_to_subtab_admin_products()

    is_disabled = AdministrationProductsPage(add_product_driver).actions_button_is_disabled()

    if is_disabled:
        AdministrationProductsPage(add_product_driver).click_to_first_checkbox()
        AdministrationProductsPage(add_product_driver).click_to_actions_button()
        AdministrationProductsPage(add_product_driver).click_to_delete_product_button()
        AdministrationProductsPage(add_product_driver).click_to_delete_product_in_modal()
        AdministrationProductsPage(add_product_driver).click_to_close_button()


    assert AdministrationProductsPage(add_product_driver).success_message.is_displayed()