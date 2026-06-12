import sys

from shared.types import PageResult
from view.page00_home import page_home
from view.page01_tri import page_tri
from view.page99_tbd import page_tbd

routeur = {
    "return_home": {"h": page_home},
    "home": {"1": page_tri, "2": page_tbd},
    "tri": {"1": page_tbd},
}


def get_next_page(page_result: PageResult):
    if page_result.next == "q":
        sys.exit()

    if page_result.next == "h":
        return page_home()

    return routeur[page_result.page][page_result.next]()
