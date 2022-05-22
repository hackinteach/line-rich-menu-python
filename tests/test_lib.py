import json
import os
from typing import List
from unittest import mock

import pytest
from line_rich_menu import LineRichMenu
from linebot.models import RichMenuResponse


def test_init_client_without_token():
    with pytest.raises(Exception) as e:
        with mock.patch.dict(os.environ, clear=True):
            menu = LineRichMenu()
            assert "No access token provided" in str(e.value)


def test_create_rich_menu(bot_client, valid_menu_path, valid_image_path):
    menu = LineRichMenu()
    with open(valid_menu_path, "r") as f:
        data = json.load(f)
    menu_id = menu.create_menu(data=data, image_path=valid_image_path)
    menus: List[RichMenuResponse] = bot_client.get_rich_menu_list()
    menu_ids = []
    for m in menus:
        menu_ids.append(m.rich_menu_id)
    assert menu_id in menu_ids
    # clean up
    bot_client.delete_rich_menu(rich_menu_id=menu_id)


def test_create_invalid_menu_object(bot_client, invalid_menu_path, valid_image_path):
    menu = LineRichMenu()
    with open(invalid_menu_path, "r") as f:
        data = json.load(f)

    menu_before = bot_client.get_rich_menu_list()

    with pytest.raises(Exception) as e:
        menu.create_menu(data=data, image_path=valid_image_path)
        assert "Invalid" in str(e.value)

    menu_after = bot_client.get_rich_menu_list()
    assert len(menu_before) == len(menu_after), "No menu should be created"


def test_create_unsupported_image(bot_client, valid_menu_path, unsupported_image_path):
    menu = LineRichMenu()
    with open(valid_menu_path, "r") as f:
        data = json.load(f)

    menu_before = bot_client.get_rich_menu_list()

    with pytest.raises(Exception) as e:
        menu.create_menu(data=data, image_path=unsupported_image_path)
        assert "Unsupported" in str(e.value)

    menu_after = bot_client.get_rich_menu_list()
    assert len(menu_before) == len(menu_after), "No menu should be created"
