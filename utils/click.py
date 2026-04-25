from appium.webdriver.common.appiumby import AppiumBy


def click_to_element(driver, element):
    element = driver.find_element(AppiumBy.XPATH, element)
    element.click()
