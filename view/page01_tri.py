import os

from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.table import Table

from model.algos.liste_algos import list_aglos
from shared.types import PageResult


def page_tri() -> PageResult:
    os.system("cls||clear")

    console = Console()
    table = Table()

    tri_main_panel = """
    Algorithmes de tri
"""
    tri_input = """
Quel est votre choix ?
>>> """

    table.add_column("Numéro", justify="right", style="cyan")
    table.add_column("Nom", style="magenta")

    for algo in list_aglos:
        table.add_row(algo.id, algo.name)

    console.print(Panel(tri_main_panel, style="color(12)", box=box.DOUBLE_EDGE))
    console.print(table)
    console.print("Veuillez choisir un aglorithme :")

    while True:
        user_input = console.input(tri_input)
        clean_input = user_input.lower().strip().split()

        if clean_input[0] == "q" or clean_input[0] == "h":
            return PageResult("tri", clean_input[0], None)

        valid_answer = [algo.id for algo in list_aglos]
        print(valid_answer)
        print(clean_input)
        if len(clean_input) != 0 and all(
            value in valid_answer for value in clean_input
        ):
            return PageResult("tri", "1", clean_input)

        else:
            console.print("Commande invalide. Veuillez faire un autre choix.")
