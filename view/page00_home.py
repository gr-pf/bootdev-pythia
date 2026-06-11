import os
import sys
import time

from rich.console import Console
from rich.panel import Panel
from rich import box

from view.page01_tri import page_tri


def page_home():
    os.system("cls||clear")

    console = Console()
    console.rule("ellipsis")

    home_main_panel = """
    PYTHIA
    Oracle de vos algos

    v. 0.1.0
"""

    home_main_content = """
Pythia est un outil CLI en Python conçu pour révéler ce qui se cache derrière les performances des algorithmes et structures de données. Il vise à comparer différentes implémentation — librairie standard, pur Python ou librairie dédiée à l'optimisation. Son objectif est d’apprendre l’algorithmie de manière concrète, expérimentale et mesurable.

Il est développé dans le cadre du programme d'apprentissage du code de boot.dev
"""

    home_choices = """
Q. Quitter
1. Algo de Tri
2. A venir
"""

    home_input = """
Quel est votre choix ?
>>> """

    console.print(Panel(home_main_panel, style="color(12)", box=box.DOUBLE_EDGE))
    console.print(home_main_content)
    console.print(home_choices)

    while True:
        user_input = console.input(home_input)
        match user_input:
            case "Q" | "q":
                console.print("Vous allez quitter Pythia...")
                time.sleep(1)
                sys.exit()

            case "1":
                console.print("Vous avez choisi : 1. Algo de Tri")
                time.sleep(0.5)
                return page_tri()

            case "2":
                console.print("Vous avez choisi : 2. A venir")
                time.sleep(0.5)
                console.print(
                    "Cette partie n'a pas encore été implémentée. Veuillez faire un autre choix."
                )

            case _:
                console.print("Commande invalide. Veuillez faire un autre choix.")


if __name__ == "__main__":
    page_home()
