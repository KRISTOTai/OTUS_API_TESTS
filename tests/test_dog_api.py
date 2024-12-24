import requests
import pytest

"""Тесты API https://dog.ceo/dog-api/"""


def test_dogs_random(base_data_for_dogs):
    random_url = 'breeds/image/random'
    response = requests.get(base_data_for_dogs.base_url + random_url)
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    print("Ответ метода GET_random: " + response.text)


def test_list_all_sub_breeds(base_data_for_dogs):
    list_all_sub_breads_url = 'breed/hound/list'
    response = requests.get(base_data_for_dogs.base_url + list_all_sub_breads_url)
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    json_for_check = response.json()
    assert base_data_for_dogs.json_dogs_sub_breed.get("message") == json_for_check.get(
        "message"), f'Ошибка: содержание "message" не совпадает'
    print(f'Ответ метода GET_all_sub-breeds: {json_for_check.get("message")}')


@pytest.mark.parametrize(("key", "value"), [('australian', ["kelpie", "shepherd"]),
                                            ('bakharwal', ["indian"]), ("bulldog", ["boston", "english", "french"])],
                         ids=[dict, dict, dict])
def test_list_all_breeds(base_data_for_dogs, key, value):
    list_all_breads_url = 'breeds/list/all'
    response = requests.get(base_data_for_dogs.base_url + list_all_breads_url)
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    json_for_check = response.json()
    assert base_data_for_dogs.json_dogs_all_breed.get("message") == json_for_check.get(
        "message"), f'Ошибка: содержание "message" не совпадает'
    assert value == response.json()['message'][key]
    print(f'Ответ метода GET_all_breeds: проверки успешны')


def test_list_all_images(base_data_for_dogs):
    list_all_images_url = 'breed/hound/images'
    response = requests.get(base_data_for_dogs.base_url + list_all_images_url)
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    json_for_check = response.json()
    assert base_data_for_dogs.json_dogs_all_images.get("message") == json_for_check.get(
        "message"), f'Ошибка: содержание "message" не совпадает'
    print(f'Ответ метода GET_all_images: проверки успешны')


@pytest.mark.parametrize("insert_word", ['african', 'bluetick', 'boxer'], ids=["string", "string", "string"])
def test_list_insert_random(base_data_for_dogs, insert_word):
    dogs_insert_random_url = f'breed/{insert_word}/images/random'
    response = requests.get(base_data_for_dogs.base_url + dogs_insert_random_url)
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    assert insert_word in response.text, f'Ошибка: ссылка на изображение не содержит ключевое слово'
    print(f'Ответ метода GET_list_insert_random: проверки успешны')


@pytest.mark.parametrize("insert_word", ['cuba', 'moscow', 'africa'], ids=["string", "string", "string"])
def test_list_insert_random_negative(base_data_for_dogs, insert_word):
    dogs_insert_random_url = f'breed/{insert_word}/images/random'
    response = requests.get(base_data_for_dogs.base_url + dogs_insert_random_url)
    assert 404 == response.status_code, f'Ошибка: ожидался статус-код 404, но получен {response.status_code}'
    print(f'Ответ метода GET_insert_random_negative: негативные проверки успешны')
