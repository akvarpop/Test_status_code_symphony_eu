import pytest
from configuration import SERVICE_URL


@pytest.fixture
def url_range(url, expected_result):
    return url, expected_result
