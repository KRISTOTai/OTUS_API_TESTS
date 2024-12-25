import requests
import pytest

"""Тесты API https://jsonplaceholder.typicode.com/"""


@pytest.mark.parametrize("user_id", [3, 5, 2], ids=['integer', 'integer', 'integer'])
def test_jsonplaceholder_users_get(base_data_for_jsonplaceholder, user_id):
    base_url, *_ = base_data_for_jsonplaceholder
    users_url = 'users'
    response = requests.get(base_url + users_url, params={'id': user_id})
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    assert len(response.json()) > 0, "Ошибка: API вернул пустой список"
    assert response.json()[0]['id'] == user_id
    print("\nОтвет метода GET_jsonplaceholder_users_get: успех")


@pytest.mark.parametrize("user_id", [3, 17], ids=["integer", "integer"])
def test_create_jsonplaceholder_posts(base_data_for_jsonplaceholder, user_id):
    base_url, headers = base_data_for_jsonplaceholder
    posts_url = 'posts'
    body = {
        "method": "POST",
        "body": {
            "title": "Управлению по управлению всеми управлениями РФ",
            "body": "я КОНКРЕТНО подзаебался",
            "userId": user_id
        },
        "headers": headers
    }
    response = requests.post(base_url + posts_url, json=body)
    assert 201 == response.status_code, f'Ошибка: ожидался статус-код 201, но получен {response.status_code}'
    print("\nОтвет метода POST_create_jsonplaceholder_posts: успех")


@pytest.mark.parametrize(("user_id", "id_"), [(2, 15), (4, 34)], ids=[tuple, tuple])
def test_jsonplaceholder_posts_get(base_data_for_jsonplaceholder, user_id, id_):
    base_url, *_ = base_data_for_jsonplaceholder
    posts_url = f'posts/{id_}'
    response = requests.get(base_url + posts_url)
    print(response.json())
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    assert response.json()['userId'] == user_id
    print("\nОтвет метода GET_jsonplaceholder_posts_get: успех")


def test_jsonplaceholder_posts_delete(base_data_for_jsonplaceholder):
    base_url, *_ = base_data_for_jsonplaceholder
    id_ = 1
    delete_url = f'posts/{id_}'
    response = requests.delete(base_url + delete_url)
    assert 200 == response.status_code, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'
    print("\nОтвет метода DELETE_jsonplaceholder_posts_delete: успех")
