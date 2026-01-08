import os

import pytest
import requests

from services.dog import DogService

url = os.getenv("DOG_URL")

@pytest.fixture(scope="module")
def dog_service():
    return DogService(base_url=url)


@pytest.mark.dog
def test_get_random_dog(dog_service):
    dog = dog_service.get_random_dog()

    assert dog.status == "success"
    assert ".jpg" in dog.message

@pytest.mark.dog
def test_get_dog_by_breed_without_params(dog_service):
    dog = dog_service.get_dog_by_breed_without_params()

    assert dog.status == "success"
    assert len(dog.message) > 0

@pytest.mark.dog
@pytest.mark.parametrize(
    "count",
    [
        pytest.param(1, id="find by count = 1"),
        pytest.param(10, id="find by count = 10"),
        pytest.param(100, id="find by count = 100"),
    ]
)
def test_get_dog_by_count(dog_service, count):
    dog = dog_service.get_dog_by_count(count)

    assert dog.status == "success"
    assert len(dog.message) == count

@pytest.mark.dog
@pytest.mark.parametrize(
    "breed",
    [
        pytest.param("borzoi", id="find by borzoi"),
        pytest.param("beagle", id="find by beagle"),
        pytest.param("akita", id="find by akita"),
        pytest.param("chow", id="find by chow"),
        pytest.param("boxer", id="find by boxer")
    ]
)
def test_get_dog_by_breed(dog_service, breed):
    dog = dog_service.get_dog_by_breed(breed)

    assert dog.status == "success"
    assert ".jpg" in dog.message

@pytest.mark.dog
@pytest.mark.parametrize(
    "breed",
    [
        pytest.param("qwe", id="find by qwe"),
        pytest.param("", id="find by empty string"),
        pytest.param("qwndqnwduqn", id="find by qwndqnwduqn"),
    ]
)
def test_not_found_dog(dog_service, breed):
    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        dog_service.get_dog_by_breed(breed)

        assert exc_info.value.response.status_code == 404