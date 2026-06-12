import os

from rich.console import Console
from rich.panel import Panel
from rich import box

from shared.types import PageResult


def page_tbd() -> PageResult:
    os.system("cls||clear")

    console = Console()

    tbd_main_panel = """
    Page non implémentée
"""
    tbd_choices = """
Q. Quitter
H. Retour Accueil
"""

    tbd_input = """
Quel est votre choix ?
>>> """

    console.print(Panel(tbd_main_panel, style="color(12)", box=box.DOUBLE_EDGE))
    console.print(tbd_choices)

    while True:
        user_input = console.input(tbd_input)
        clean_input = user_input.lower().strip()

        if clean_input == "q":
            return PageResult("tbd", "q", None)

        return PageResult("tbd", "h", None)
