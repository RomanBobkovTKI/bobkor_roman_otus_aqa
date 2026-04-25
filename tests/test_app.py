import allure

from utils.click import click_to_element
from utils.scroll import scroll_to_element

@allure.feature("Calendar app")
@allure.story("Open app")
def test_open_app(appium_driver):
    with allure.step("Открыть приложение"):
        pass
    assert appium_driver.current_package == "com.csdroid.pkg"

@allure.feature("Calendar app")
@allure.story("Open calendar")
def test_open_calendar_after_scroll_by_1_step(appium_driver):
    with allure.step("Доскроллить до календаря"):
        scroll_to_element(appium_driver, "com.csdroid.pkg:id/tv_title", "Calendar", 1)
    with allure.step("Нажать на календарь"):
        click_to_element(
        appium_driver,
        '//android.widget.TextView[@resource-id="com.csdroid.pkg:id/tv_title" and @text="Calendar"]',
    )
    with allure.step("Подтвердить открытие"):click_to_element(
        appium_driver, '//android.widget.Button[@resource-id="android:id/button1"]'
    )

    assert appium_driver.current_package in [
        "com.google.android.gms",
        "com.google.android.calendar",
    ]
