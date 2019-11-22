from os import environ, path, listdir
from typing import Dict, Any

from linebot.api import LineBotApi
from linebot.models import (RichMenu, RichMenuArea,
                            RichMenuBounds, RichMenuSize, URIAction, PostbackAction, Action)
import json
import dotenv

dotenv.load_dotenv()
# TODO put LINE_ACCESS_TOKEN in .env file
api = LineBotApi(environ.get("LINE_ACCESS_TOKEN"))

# TODO Edit this path accordingly
base_directory = "./rich_menu_img"

# TODO Edit template file
template_file = 'template.json'

if template_file not in listdir('.'):
    raise FileNotFoundError("Template file not found")

mx = json.load(open(template_file, 'r'))


def do_create(menus: Dict[Any, Any],
              img_type: str = "png",
              base_path: str = "./",
              write_to_file: bool = True,
              output_file_name: str = "rich_menu_result_id") -> Dict[str, str]:
    """
    Create rich menu and set its image

    example menu dictionary
    image name: "awesomeImage.png"

    {
        "awesomeImage": {
            "size": {
                "width": 2500,
                "height": 1686
            },
            "selected": True,
            "name": "MyAwesomeRichMenu",
            "chatBarText": "Touch me!",
            "areas": [
                {
                    "bounds": {
                        "x": 0,
                        "y": 0,
                        "width": 2500,
                        "height": 1686
                    },
                    "action": {
                        "type": "uri",
                        "uri": "https://github.com/hackinteach"
                    }
                }
            ]
        },
        ...
    }

    :param base_path: directory that stores images
    :param menus: dictionary containing {"file_name" : {content from Line Bot Designer}
    :param img_type: "png" or "jpg"
    :param write_to_file: Should I write dict[menu_name, menu_id] to file
    :param output_file_name: output file name for id result
    :return: resulting dictionary of (name, id) for the created menus
    """

    result_ids = dict()
    for filename, template in menus.items():
        print("Processing", filename)
        try:
            m = RichMenu(
                size=RichMenuSize(width=template["size"]["width"], height=template["size"]["height"]),
                selected=False,  # override from template
                name=template["name"],
                chat_bar_text=template["chatBarText"],
                areas=template["areas"]
            )
            menu_id = api.create_rich_menu(rich_menu=m)

            print(template["name"], "->", menu_id)
            result_ids[template["name"]] = menu_id

            with open(path.join(base_path, f"{filename}.{img_type}"), "rb") as img_file:
                api.set_rich_menu_image(rich_menu_id=menu_id,
                                        content_type=f"image/{img_type}",
                                        content=img_file)

            print("==="*10)
        except Exception as e:
            print(e)
            continue
    print("results:", result_ids)
    if write_to_file:
        if ".json" not in output_file_name:
            output_file_name += ".json"
        json.dump(result_ids, open(output_file_name, "w"))
    return result_ids


do_create(mx, base_path=base_directory)

