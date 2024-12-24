import json
import pytest
from files import JSON_FILE_all_sub_breeds, JSON_FILE_all_breeds, JSON_FILE_all_images, JSON_FILE_breweries_id
from dataclasses import dataclass
import requests


@dataclass
class BaseData:
    base_url: str
    json_dogs_sub_breed: dict
    json_dogs_all_breed: dict
    json_dogs_all_images: dict


@pytest.fixture(scope='session', autouse=True)
def create_data_for_autouse():
    print('\nНачало тестов')
    yield
    print('\nОкончание тестов')


@pytest.fixture()
def base_data_for_dogs():
    base_url = 'https://dog.ceo/api/'
    with open(JSON_FILE_all_sub_breeds, "r") as f:
        json_dogs_sub_breed = json.load(f)
    with open(JSON_FILE_all_breeds, "r") as f:
        json_dogs_all_breed = json.load(f)
    with open(JSON_FILE_all_images, "r") as f:
        json_dogs_all_images = json.load(f)
    yield BaseData(base_url, json_dogs_sub_breed, json_dogs_all_breed, json_dogs_all_images)


@pytest.fixture()
def base_data_for_brew():
    base_url = 'https://api.openbrewerydb.org/v1/breweries/'
    with open(JSON_FILE_breweries_id, "r") as f:
        json_breweries_id = json.load(f)
    yield base_url, json_breweries_id


@pytest.fixture()
def base_data_for_jsonplaceholder():
    base_url = 'https://jsonplaceholder.typicode.com/'
    headers = {
        "Content-type": "application/json; charset=UTF-8",
    }
    yield base_url, headers


# Задание часть 2
def pytest_addoption(parser):
    """Добавление кастомных опций для pytest."""
    parser.addoption(
        "--url", action="store", default="https://ya.ru", help="URL to test"
    )
    parser.addoption(
        "--status_code", action="store", type=int, default=200, help="Expected status code"
    )


@pytest.fixture()
def url_and_status_code(request):
    """Фикстура для получения URL и ожидаемого статус-кода."""
    url = request.config.getoption("--url")
    status_code = request.config.getoption("--status_code")
    return url, status_code


def test_url_status(url_and_status_code):
    url, expected_status_code = url_and_status_code
    response = requests.get(url)
    assert response.status_code == expected_status_code, f"Статус отличен от ожидаемого: {expected_status_code}"
    print("test_url_status - успех")
