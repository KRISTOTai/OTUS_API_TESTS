import requests
import pytest

"""Тесты API https://www.openbrewerydb.org/"""


@pytest.mark.parametrize("count", [3, 5, 2], ids=['integer', 'integer', 'integer'])
def test_breweries_random(base_data_for_brew, count):
    base_url, *_ = base_data_for_brew
    random_url = 'random'
    response = requests.get(base_url + random_url, params={'size': count})
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    count_of_dict = 0
    for f in response.json():
        count_of_dict += 1
    assert count_of_dict == count, f'Количество выходных данных отличается от ожидаемого'
    print("\nОтвет метода GET_breweries_random: успех")


@pytest.mark.parametrize(("country", "count"), [('South Korea', 2), ('United States', 7), ('Sweden', 1)],
                         ids=[dict, dict, dict])
def test_breweries_by_country(base_data_for_brew, country, count):
    base_url, *_ = base_data_for_brew
    response = requests.get(base_url, params={'by_country': country, 'per_page': count})
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    assert len(response.json()) == count, f'Ошибка: ожидалось {count} записей, но получено {len(response.json())}'
    assert country in response.text, f'Ошибка: ссылка на изображение не содержит ключевое слово'
    print("\nОтвет метода GET_breweries_by_country: успех")


def test_breweries_by_id(base_data_for_brew):
    base_url, json_breweries_id = base_data_for_brew
    id_url = 'b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'
    response = requests.get(base_url + id_url)
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    assert json_breweries_id == response.json(), f'Ошибка: содержание json не совпадает'
    print("\nОтвет метода GET_breweries_by_id: успех")


def test_breweries_by_postal(base_data_for_brew):
    base_url, *_ = base_data_for_brew
    postal = '92101'
    response = requests.get(base_url, params={'by_postal': postal, 'per_page': 2})
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    assert postal in response.text, f'Ошибка: postal code отсутствует в тексте'
    print("\nОтвет метода GET_breweries_by_postal: успех")


def test_breweries_by_dist(base_data_for_brew):
    base_url, *_ = base_data_for_brew
    latitude = 32.88313237
    longitude = -117.1649842
    response = requests.get(base_url, params={'by_dist': f'{latitude}, {longitude}', 'per_page': 2})
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    assert str(latitude) in response.text, f'Ошибка: latitude отсутствует в тексте'
    assert str(longitude) in response.text, f'Ошибка: longitude отсутствует в тексте'
    print("\nОтвет метода GET_breweries_by_dist: успех")


@pytest.mark.skip(reason='bag, пустой ответ')
@pytest.mark.parametrize(("country", "count"), [('Moscow', -2), ('Novgorod', -7), ('Paris', -1)],
                         ids=[dict, dict, dict])
def test_breweries_by_country_negative(base_data_for_brew, country, count):
    base_url, *_ = base_data_for_brew
    response = requests.get(base_url, params={'by_country': country, 'per_page': count})
    assert 404 == response.status_code, f'Ошибка: ожидался статус-код 404, но получен {response.status_code}'
    print("\nОтвет метода GET_breweries_by_country_negative: успех")
