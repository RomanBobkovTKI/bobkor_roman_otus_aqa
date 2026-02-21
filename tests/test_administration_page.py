import pytest

from fixtures.driver import driver
from fixtures.login_to_admin import admin_login, product_admin_driver
from page_object_model.administration_login_page import AdministrationPage
from page_object_model.administration_main_page import AdministrationMainPage
from page_object_model.administration_products_page import AdministrationProductsPage
from page_object_model.base_page import BasePage
from utils.asserts.assert_text_equals import assert_element_text_equals
from utils.product import get_random_product


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_email_input_is_desplayed(driver):
    expected_email_label = "email address"

    assert AdministrationPage(driver).email_input.is_displayed(), (
        f"Не отображается инпут ввода мейла"
    )
    assert_element_text_equals(AdministrationPage(driver).email_label.text, expected_email_label)


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_password_input_is_desplayed(driver):
    expected_password_label = "password"

    assert AdministrationPage(driver).password_input.is_displayed(), (
        f"Не отображается инпут ввода пароля"
    )
    assert_element_text_equals(AdministrationPage(driver).password_label.text, expected_password_label)


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_login_button_is_desplayed(driver):
    expected_login_label = "log in"

    assert_element_text_equals(AdministrationPage(driver).login_button.text, expected_login_label)
    assert AdministrationPage(driver).login_button.is_displayed(), (
        f"Не отображается кнопка логина"
    )


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_click_to_forgot_pass(driver):
    admin_page = AdministrationPage(driver)
    expected_forgot_password_text = "i forgot my password"
    actual_text = admin_page.forgot_pass_link.text
    admin_page.click_to_forgot_pass()

    assert_element_text_equals(actual_text, expected_forgot_password_text)
    assert admin_page.reset_pass_button.is_displayed(), (
        f"Не видна кнопка восстановления пароля"
    )


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_stay_logged_in(driver):
    expected_text = "stay logged in"

    assert_element_text_equals(AdministrationPage(driver).stay_logged_in_label.text, expected_text)
    assert AdministrationPage(driver).stay_logged_in_label.is_displayed(), (
        f"Не отображается надпись {'stay logged in'}"
    )


@pytest.mark.administration_page
@pytest.mark.parametrize("presta_shop_url", [AdministrationPage.URL], indirect=True)
def test_login(driver):
    admin_page = AdministrationPage(driver)
    expected_dashboard_header = "dashboard"
    expected_url_path = "administration/?controller=AdminDashboard"

    admin_page.clear_email_input()
    admin_page.clear_password_input()
    # вот тут наверно нужен какой-то дата сет с тестовыми данными
    admin_page.send_keys_to_email("admin@example.com")
    admin_page.send_keys_to_password("Admin123!")
    admin_page.click_to_log_in_button()

    assert_element_text_equals(AdministrationMainPage(driver).dashboard_header.text, expected_dashboard_header)
    assert AdministrationMainPage(driver).dashboard_header.is_displayed()
    assert expected_url_path in BasePage(driver).current_url


@pytest.mark.administration_page
def test_logout(admin_login):
    admin_main_page = AdministrationMainPage(admin_login)
    expected_url_path = "/administration/login"

    admin_main_page.click_to_profile_icon()
    admin_main_page.click_logout_button()
    AdministrationPage(admin_login).login_logo

    assert expected_url_path in BasePage(admin_login).current_url


@pytest.mark.administration_page
def test_add_new_product(admin_login):
    admin_main_page = AdministrationMainPage(admin_login)
    admin_product_page = AdministrationProductsPage(admin_login)
    product = get_random_product()

    admin_main_page.click_to_subtab_admin_catalog()
    admin_main_page.click_to_subtab_admin_products()
    admin_product_page.click_add_new_product()
    admin_product_page.click_add_new_product_in_modal()

    admin_product_page.clear_product_name()

    admin_product_page.send_keys_to_product_name(
        product["product_name"]
    )

    admin_product_page.click_to_save_product_button()

    assert admin_product_page.success_message.is_displayed(), ()


@pytest.mark.administration_page
def test_delete_product(product_admin_driver):
    admin_main_page = AdministrationMainPage(product_admin_driver)
    admin_product_page = AdministrationProductsPage(product_admin_driver)
    admin_main_page.click_to_subtab_admin_catalog()
    admin_main_page.click_to_subtab_admin_products()

    is_disabled = admin_product_page.actions_button_is_disabled()

    if is_disabled:
        admin_product_page.click_to_first_checkbox()
        admin_product_page.click_to_actions_button()
        admin_product_page.click_to_delete_product_button()
        admin_product_page.click_to_delete_product_in_modal()
        admin_product_page.click_to_close_button()

    assert AdministrationProductsPage(product_admin_driver).success_message.is_displayed()