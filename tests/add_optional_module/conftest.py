def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="url for send requests"
    )

    parser.addoption(
        "--status_code",
        action="store",
        default="200",
        help="expected status code"
    )
