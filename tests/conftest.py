import pytest

from line_rich_menu.menu import LineRichMenu


@pytest.fixture()
def client() -> LineRichMenu:
    return LineRichMenu()
