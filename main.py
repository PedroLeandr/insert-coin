import os
import time

import studios

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(
            "============================\n"
            f"{'Insert Coin':^28}\n"
            "============================\n"
            "1. Estudios\n"
            "0. Sair\n"
            "============================\n"
        )
        try:
            choice = int(input("Opção: "))

            match choice:
                case 1:
                    studios.menu_studios()

                case 0:
                    print("Saiste")
                    return

                case _:
                    print("404")
                    time.sleep(3)

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("deve inserir um numero!")
            time.sleep(3)
            


if __name__ == "__main__":
    main_menu()
