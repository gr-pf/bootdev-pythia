import os
import sys
import time


def main():
    columns, lines = os.get_terminal_size()

    if columns < 80:
        warning_size = f"""Le terminal a une taille de {columns} colonnes !
Il faut un terminal d'au moins 80 colonnes pour un affichage correct.        
"""
        print(warning_size)
        prefix = ""
        while True:
            user_input = input(f"{prefix}Souhaitez-vous continuer ? (y/n) ")
            if user_input == "y" or user_input == "Y":
                break
            elif user_input == "n" or user_input == "N":
                sys.exit()

            prefix = "Vous devez saisir Yes (y) ou No (n) - "

    print("Le programme va démarrer...")
    time.sleep(1)
    os.system("cls||clear")


if __name__ == "__main__":
    main()
