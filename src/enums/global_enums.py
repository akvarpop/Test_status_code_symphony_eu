from enum import Enum


class GlobalErrorMassages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected'
    WRONG_URL_HTTPS = 'Redirect from http didnt work to https'
