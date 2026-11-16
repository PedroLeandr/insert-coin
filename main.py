import os
import time

import studios

def main_menu():
    """Apresenta o menu principal e encaminha o utilizador para os submenus."""
    # Repete o menu quando um submenu termina ou a opção é inválida.
    while True:
        # Usa o comando de limpeza adequado ao sistema operativo.
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
                    # A execução continua aqui quando o submenu devolve o controlo.
                    studios.menu_studios()

                case 0:
                    print("Saiste")
                    # Termina a função e, neste ponto de entrada, o programa.
                    return

                case _:
                    print("404")
                    time.sleep(3)

        except ValueError:
            # int() rejeita entradas como letras ou uma resposta vazia.
            os.system('cls' if os.name == 'nt' else 'clear')
            print("deve inserir um numero!")
            time.sleep(3)
            


# Inicia a aplicação apenas quando este ficheiro é executado diretamente.
if __name__ == "__main__":
    main_menu()
