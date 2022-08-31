import pytest
import requests
from configuration import SERVICE_URL, ALL_URL_LIST, WRONG_URL_HTTPS
from src.enums.global_enums import GlobalErrorMassages
import json


@pytest.mark.parametrize('url', WRONG_URL_HTTPS)
def test_url_redirect_to_https(url):
    response = requests.get(url=url)
    assert response.url == SERVICE_URL, GlobalErrorMassages.WRONG_URL_HTTPS.value

@pytest.mark.parametrize('url', ALL_URL_LIST)
def test_get_status_code_all_pages(url):
    response = requests.get(url=SERVICE_URL+url)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value


# Как с xml вытянуть url и записать их в лист, (может import json, но не вышло)
#нужно ставить url=   (url=SERVICE_URL+url)


# def test_get_xml():
#     response = requests.get(url=XML_URL)
#     text_json = response.text.
#     #obj = json.loads(text_json)
#     print(text_json)
#     #print(obj)

