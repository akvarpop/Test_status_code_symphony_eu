"""
Testing the work of redirects from http to https and incorrect slash field data
Тестуємо роботу редіректів з http на https та некоректні данні піля слешу
"""
import pytest
import requests
from configuration import SERVICE_URL, WRONG_URL_HTTPS, \
    WRONG_URL_AFTER_SLASH
from src.enums.global_enums import GlobalErrorMassages



@pytest.mark.parametrize('url', WRONG_URL_AFTER_SLASH)
def test_entering_incorrect_data_in_the_url_after_the_slash(url):
    """
    При введені некоректних данних піля слешу в полі url повинно перенаправити на сторінку 404
    When entering incorrect data after a slash in the url field, it should redirect to a 404 page
    """
    response = requests.get(SERVICE_URL + url)
    assert response.status_code == 404, GlobalErrorMassages.WRONG_STATUS_CODE.value


@pytest.mark.parametrize('url', WRONG_URL_HTTPS)
def test_url_redirect_to_https(url):
    """
    Переірка роботи редіректі з http, www на сторінку з  hhtps
    Checking the operation of redirects from http, www to a page with https
    """
    response = requests.get(url)
    assert response.url == SERVICE_URL, GlobalErrorMassages.WRONG_URL_HTTPS.value





