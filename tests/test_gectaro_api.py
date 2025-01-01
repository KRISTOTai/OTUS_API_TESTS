import requests
import pytest


def test_gectaro_get_resource_requests(request, gectaro_key_project):
    baseurl = request.config.getoption('--url')
    project, key = gectaro_key_project
    url = baseurl + project + 'resource-requests'
    response = requests.get(url, headers={'Authorization': key})
    assert response.status_code == requests.codes.ok, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'


@pytest.mark.parametrize("unnormal_key", ['_xbYD3PwYW0N11-ycESdZY0eFudvy-QE'], ids=['string'])
def test_gectaro_get_resource_requests_neg(request, gectaro_key_project, unnormal_key):
    baseurl = request.config.getoption('--url')
    project, key = gectaro_key_project
    url = baseurl + project + 'resource-requests'
    response = requests.get(url, headers={'Authorization': unnormal_key})
    assert response.status_code == requests.codes.unauthorized, f'Ошибка: ожидался статус-код 401, но получен {response.status_code}'
    assert response.json().get(
        'name') == 'Unauthorized', f'Ошибка: ожидался текст: Unauthorized, но получен {response.json().get['name']}'


@pytest.mark.parametrize(("volume", "cost", "needed_at", "batch_number"),
                         [(2, 30, "30122024", 3), (4, 40, "1012025", 5)],
                         ids=["request1", "request2"])
def test_gectaro_post_resource_requests(request, gectaro_key_project, volume, cost, needed_at, batch_number):
    baseurl = request.config.getoption('--url')
    project, key = gectaro_key_project
    url = baseurl + project + 'resource-requests'
    body = {
        'project_tasks_resource_id': '6910',
        'volume': str(volume),
        'cost': str(cost),
        'needed_at': needed_at,
        'batch_number': str(batch_number),
        'batch_parent_request_id': '',
        'is_over_budget': '0'
    }
    response = requests.post(url, headers={'Content - type': 'application/json', 'Authorization': key}, data=body)
    assert response.status_code == requests.codes.created, f'Ошибка: ожидался статус-код 201, но получен {response.status_code}'


@pytest.mark.skip(reason='не создается заявка')
@pytest.mark.parametrize("id_", [10418179], ids=['integer'])
def test_gectaro_get_resource_request_id(request, gectaro_key_project, id_):
    baseurl = request.config.getoption('--url')
    project, key = gectaro_key_project
    url = baseurl + project + 'resource-requests/' + f'{id_}'
    response = requests.get(url, headers={'Authorization': key})
    assert response.status_code == requests.codes.ok, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'


@pytest.mark.parametrize("id_", [9999, ''], ids=['integer', 'string'])
def test_gectaro_get_resource_request_id_neg(request, gectaro_key_project, id_):
    baseurl = request.config.getoption('--url')
    project, key = gectaro_key_project
    url = baseurl + project + 'resource-requests/' + f'{id_}'
    response = requests.get(url, headers={'Authorization': key})
    if response.status_code == 404:
        print(f'Статус код согласно ожиданиям {response.status_code}')
    elif response.status_code == 405:
        print(f'Статус код согласно ожиданиям {response.status_code}')
    else:
        print(f'Провал, неожиданный код {response.status_code}')


@pytest.mark.skip(reason='не создается заявка')
@pytest.mark.parametrize(("id_", "volume", "cost", "needed_at", "batch_number"),
                         [(10418173, '7', '70', '30122024', '8'), (10418174, '8', '50', '2012025', '9')],
                         ids=[tuple, tuple])
def test_gectaro_put_resource_requests(request, gectaro_key_project, volume, cost, needed_at, batch_number, id_):
    baseurl = request.config.getoption('--url')
    project, key = gectaro_key_project
    url = baseurl + project + 'resource-requests/' + f'{id_}'
    body = {
        'project_tasks_resource_id': '6910',
        'volume': volume,
        'cost': cost,
        'needed_at': needed_at,
        'batch_number': batch_number,
        'batch_parent_request_id': '',
        'is_over_budget': '0'
    }
    response = requests.post(url, headers={'Authorization': key, 'Content-Type': 'multipart/form-data'}, json=body)
    assert response.status_code == requests.codes.ok, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'


@pytest.mark.parametrize(("id_", "volume", "cost", "needed_at", "batch_number"),
                         [('', '7', '70', '30122024', '8'), (10418174, '-8', '50', '2012025', '9')],
                         ids=[tuple, tuple])
def test_gectaro_put_resource_requests_neg(request, gectaro_key_project, volume, cost, needed_at, batch_number, id_):
    baseurl = request.config.getoption('--url')
    project, key = gectaro_key_project
    url = baseurl + project + 'resource-requests/' + f'{id_}'
    body = {
        'project_tasks_resource_id': '6910',
        'volume': volume,
        'cost': cost,
        'needed_at': needed_at,
        'batch_number': batch_number,
        'batch_parent_request_id': '',
        'is_over_budget': '0'
    }
    response = requests.post(url, headers={'Authorization': key, 'Content-Type': 'multipart/form-data'}, json=body)
    assert response.status_code in (404, 405), f'Статус код вне пределов ожидания и равен {response.status_code}'


@pytest.mark.skip(reason='не создается заявка')
@pytest.mark.parametrize("id_", [10418173, 10418174], ids=['integer', 'integer'])
def test_gectaro_delete_resource_request_id(request, gectaro_key_project, id_):
    baseurl = request.config.getoption('--url')
    project, key = gectaro_key_project
    url = baseurl + project + 'resource-requests/' + f'{id_}'
    response = requests.get(url, headers={'Authorization': key})
    assert response.status_code == requests.codes.ok, f'Ошибка: ожидался статус-код 200, но получен {response.status_code}'


@pytest.mark.parametrize("id_", [9996, 7567], ids=['integer', 'integer'])
def test_gectaro_delete_resource_request_id_neg(request, gectaro_key_project, id_):
    baseurl = request.config.getoption('--url')
    project, key = gectaro_key_project
    url = baseurl + project + 'resource-requests/' + f'{id_}'
    response = requests.get(url, headers={'Authorization': key})
    assert response.status_code == requests.codes.not_found, f'Ошибка: ожидался статус-код 404, но получен {response.status_code}'
