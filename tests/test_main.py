from fixtures.driver import driver
from fixtures.url import presta_shop_url


def test_main_page(driver, presta_shop_url):
    driver.get(presta_shop_url)
    assert driver.title == "PrestaShop"
