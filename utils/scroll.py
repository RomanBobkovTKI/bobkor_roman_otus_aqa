from appium.webdriver.common.appiumby import AppiumBy


def scroll_to_element(driver, element_name_by_scroll, name_find_element, step=1):
    while True:
        elements = driver.find_elements(AppiumBy.ID, element_name_by_scroll)
        driver.swipe(
            elements[step].rect["x"],
            elements[step].rect["y"],
            elements[0].rect["x"],
            elements[0].rect["y"],
        )
        elements = driver.find_elements(AppiumBy.ID, element_name_by_scroll)
        elements_name = [name.text for name in elements]

        if name_find_element in elements_name:
            break
