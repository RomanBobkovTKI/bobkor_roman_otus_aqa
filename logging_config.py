import logging
from pathlib import Path


def setup_logging(log_level: str = "INFO", log_file: str = "logs/automation.log"):
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(log_level.upper())

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level.upper())
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="a")
    file_handler.setLevel(log_level.upper())
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    NOISY_LOGGERS = [
        "selenium",
        "urllib3",
        "webdriver_manager",
        "httpx",
        "httpcore",
        "blinker",
        "werkzeug",
    ]

    for name in NOISY_LOGGERS:
        logging.getLogger(name).setLevel(logging.WARNING)

    YOUR_MODULES = [
        "pages",
        "fixtures",
        "tests",
        "config",
        "__main__",
    ]

    for name in YOUR_MODULES:
        logging.getLogger(name).setLevel(logging.DEBUG)

    logging.info(f"🔧 Logging initialized. Level: {log_level}")
