"""
Тестуемо усі сторінки сайту:https://www.symphony-solutions.eu/ на статус код 200
We test all pages of the site: https://www.symphony-solutions.eu/ for status code 200
"""
"""
Для запуску усіх тестів в терміналі:pytest -v -s C:\Test_status_code_symphony_com\tests
Для запуску тестів в файл з збереженням файлу Allure: 
pytest -v -s C:\Test_status_code_symphony_eu --alluredir=allure_ss_eu
Збгенерувати посилання на звіт по тестах: allure serve allure_ss_eu
"""
import pytest
import requests
from configuration import SERVICE_URL, ALL_POST_URL, ALL_MAIN_PAGE_URL, \
    ALL_VACANCIES_URL, ALL_COUNTRY_URL, ALL_VACANCIES_CATEGORY_URL, STANDBY_UKRAINE
from src.enums.global_enums import GlobalErrorMassages
import json


@pytest.mark.parametrize('url', ALL_POST_URL)
def test_get_status_code_post_pages(url):
    response = requests.get(url=SERVICE_URL + url)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value


@pytest.mark.parametrize('url', ALL_MAIN_PAGE_URL)
def test_get_status_code_main_pages(url):
    response = requests.get(SERVICE_URL + url)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value


@pytest.mark.parametrize('url', ALL_VACANCIES_URL)
def test_get_status_code_main_pages(url):
    response = requests.get(SERVICE_URL + url)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value


@pytest.mark.parametrize('url', ALL_COUNTRY_URL)
def test_get_status_code_main_pages(url):
    response = requests.get(SERVICE_URL + url)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value


@pytest.mark.parametrize('url', ALL_VACANCIES_CATEGORY_URL)
def test_get_status_code_main_pages(url):
    response = requests.get(SERVICE_URL + url)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value


def test_get_status_code_standby_ukraine():
    response = requests.get(STANDBY_UKRAINE)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value



