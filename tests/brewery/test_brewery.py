import os

import pytest
import requests
from dotenv import load_dotenv

from services.brewery import BreweryService

load_dotenv()
url = os.getenv("BREWERY")


@pytest.fixture(scope="session")
def brewery_service():
    return BreweryService(base_url=url)


@pytest.mark.brewery
@pytest.mark.parametrize(
    "brewery_id",
    [
        pytest.param("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", id="get brewery by id"),
    ],
)
def test_get_brewery(brewery_service, brewery_id):
    brewery = brewery_service.get_brewery(brewery_id)

    assert brewery.id == brewery_id


@pytest.mark.brewery
@pytest.mark.parametrize(
    "brewery_id",
    [
        pytest.param("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e1", id="get brewery by id"),
    ],
)
def test_not_found_brewery(brewery_service, brewery_id):
    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        brewery_service.get_brewery(brewery_id)

        assert exc_info.value.response.status_code == 404


@pytest.mark.brewery
def test_get_brewery_list(brewery_service):
    brewery_list = brewery_service.get_brewery_list()

    assert len(brewery_list) >= 1


@pytest.mark.brewery
@pytest.mark.parametrize(
    "name",
    [
        pytest.param("san_diego", id="get brewery by name"),
    ],
)
def test_get_brewery_by_id(brewery_service, name):
    brewery_list = brewery_service.get_brewery_by_name(name)

    assert len(brewery_list) >= 1
