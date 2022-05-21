import json
from os import environ
from typing import List

from linebot import LineBotApi
from linebot.models import RichMenuResponse

from line_rich_menu import LineRichMenu
from line_rich_menu.const import ACCESS_TOKEN_KEY


def test_create_rich_menu():
    menu = LineRichMenu()
    with open("tests/assets/valid_menu.json", "r") as f:
        data = json.load(f)
    menu_id = menu.create_menu(data=data, image_path="tests/assets/test_menu.jpeg")
    token = environ.get(ACCESS_TOKEN_KEY)
    client = LineBotApi(token)
    menus: List[RichMenuResponse] = client.get_rich_menu_list()
    menu_ids = []
    for m in menus:
        menu_ids.append(m.rich_menu_id)
    assert menu_id in menu_ids
    # clean up
    client.delete_rich_menu(rich_menu_id=menu_id)
