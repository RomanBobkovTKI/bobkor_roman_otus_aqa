from dotenv import load_dotenv


def pytest_configure():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="choose browser: chrome, firefox or safari",
    )

    parser.addoption(
        "--url",
        action="store",
        default="default",
        help="url of PrestaShop",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="run in headless mode",
    )
