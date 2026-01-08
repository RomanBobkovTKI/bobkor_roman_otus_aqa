import os

import pytest
import requests

from services.brewery import BreweryService

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

@pytest.mark.brewery
@pytest.mark.parametrize(
    "brewery_size",
    [
        pytest.param(1, id="get brewery by random, size = 1"),
        pytest.param(30, id="get brewery by random, size = 30"),
        pytest.param(0, id="get brewery by random, size = 30"),
    ]
)
def test_get_brewery_by_random(brewery_service, brewery_size):
    brewery_list = brewery_service.get_brewery_by_random(size=brewery_size)
    print(brewery_list)

    assert len(brewery_list) == brewery_size

@pytest.mark.brewery
def test_get_brewery_by_random(brewery_service):
    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        brewery_service.get_brewery_by_random(100)

        assert exc_info.value.response.status_code == 400