import studios
import games

from menu_display import choose_menu

def main_menu():
    """Apresenta o menu principal e encaminha o utilizador para os submenus."""
    # Volta ao menu principal quando o submenu escolhido termina.
    while True:
        choice = choose_menu(None, [(1, "Estúdios"), (2, "Jogos"), (0, "Sair")])

        match choice:
            case 1:
                studios.menu_studios()
            case 2:
                games.menu_games()
            case 0:
                print("Saíste do programa.")
                return

# Inicia a aplicação apenas quando este ficheiro é executado diretamente.
if __name__ == "__main__":
    main_menu()
