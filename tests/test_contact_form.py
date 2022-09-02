import pytest
import requests
from configuration import CONTACT_FORM_URL


@pytest.mark.skip
def test_get_text():
    response = requests.post(CONTACT_FORM_URL)
    assert response.status_code == 200
    if response.status_code == 200:
        return response.text
