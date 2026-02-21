from utils.wait_element import wait_element


def login_to_admin(driver, base_url):
    admin_url = f"{base_url.rstrip('/')}/administration/login?_token="  # или как у вас называется папка
    driver.get(admin_url)

    email_input = wait_element("#email", driver)
    password_input = wait_element("#passwd", driver)
    login_button = wait_element("#submit_login", driver)

    email_input.clear()
    password_input.clear()

    # вот тут наверно нужен какой-то дата сет с тестовыми данными
    email_input.send_keys("admin@example.com")
    password_input.send_keys("Admin123!")

    login_button.click()

    wait_element("h1.page-title", driver, timeout=10)