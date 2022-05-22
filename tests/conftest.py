from os import environ

import pytest
from line_rich_menu.const import ACCESS_TOKEN_KEY
from linebot import LineBotApi


@pytest.fixture()
def bot_client() -> LineBotApi:
    token = environ.get(ACCESS_TOKEN_KEY)
    return LineBotApi(token)


@pytest.fixture()
def valid_menu_path() -> str:
    return "tests/assets/valid_menu.json"


@pytest.fixture()
def invalid_menu_path() -> str:
    return "tests/assets/invalid_menu.json"


@pytest.fixture()
def valid_image_path() -> str:
    return "tests/assets/test_menu.jpeg"


@pytest.fixture()
def unsupported_image_path() -> str:
    return "tests/assets/invalid_menu.json"
