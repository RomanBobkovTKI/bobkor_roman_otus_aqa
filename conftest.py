import logging

from dotenv import load_dotenv


def pytest_configure():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    load_dotenv()
