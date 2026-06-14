from rich.console import Console
from rich.panel import Panel
from rich import box

from shared.types import PageResult


def page_tri_iter() -> PageResult:
    console = Console()

    text_main_panel = """
    Algorithmes de tri
    Choix des paramètres des tests
"""
    text_input_size = """
Veuillez choisir la taille de la liste à trier : 
>>> """

    text_input_iter = """
Veuillez choisir la taille de la liste à trier : 
>>> """

    console.print(Panel(text_main_panel, style="color(12)", box=box.DOUBLE_EDGE))

    size = 0
    iterations = 0

    while not size:
        user_input_size = console.input(text_input_size)
        try:
            int(user_input_size)
            if int(user_input_size) <= 10000:
                size = int(user_input_size)
        except ValueError:
            console.print("Vous devez saisir un entier inférieur ou égal à 10000")

    while not iterations:
        user_input_iter = console.input(text_input_iter)
        try:
            int(user_input_iter)
            if int(user_input_iter) <= 20:
                iterations = int(user_input_iter)
        except ValueError:
            console.print("Vous devez saisir un entier inférieur ou égal à 20")

    return PageResult("tri_iter", "1", {"size": size, "iter": iterations})
