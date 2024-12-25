import requests


def test_url_status(url_and_status_code):
    url, expected_status_code = url_and_status_code
    response = requests.get(url)
    assert response.status_code == expected_status_code, f"Статус отличен от ожидаемого: {expected_status_code}"
    print("\ntest_url_status - успех")
