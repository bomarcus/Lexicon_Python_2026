import unittest

from show_menu import show_menu

test_menu = {
    "title": "TEST MENU",
    "options": {
        "0": "close",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
    },
}


class TestShowMenu(unittest.TestCase):
    def test_menu_title(self):
        show_menu(test_menu)
