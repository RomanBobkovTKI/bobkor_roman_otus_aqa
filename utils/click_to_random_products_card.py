import random


def click_to_random_elements(driver, search_func, selector):
    products_card = search_func(selector, driver)
    products_card[random.randint(0, len(products_card) - 1)].click()
