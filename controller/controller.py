from shared.types import PageResult
from controller.routeur import get_next_page


def run():
    current_page = PageResult("return_home", "h")

    while True:
        current_page = get_next_page(current_page)
