import os
import sys
import time

from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.table import Table

from model.algos.liste_algos import list_aglos
from view.page00_home import page_home


def page_tri():
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
        table.add_row(algo[0], algo[1])

    console.print(Panel(tri_main_panel, style="color(12)", box=box.DOUBLE_EDGE))
    console.print(table)
    console.print("Veuillez choisir un aglorithme :")

    while True:
        user_input = console.input(tri_input)
        match user_input:
            case "Q" | "q":
                console.print("Vous allez quitter Pythia...")
                time.sleep(1)
                sys.exit()

            case "H" | "h":
                return page_home()

            case "1":
                return

            case "2":
                return

            case "3":
                return

            case "4":
                return

            case "5":
                return

            case "6":
                return

            case "7":
                return

            case "8":
                return

            case _:
                console.print("Commande invalide. Veuillez faire un autre choix.")


if __name__ == "__main__":
    page_tri()
