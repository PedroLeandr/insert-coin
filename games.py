import json
import math
import time
from datetime import datetime
from pathlib import Path

from menu_display import choose_menu
from studios import list_studios


def menu_games():
    # Volta a mostrar o menu quando termina uma operação.
    while True:
        choice = choose_menu("Jogos", [
            (1, "Adicionar"), (2, "Listar jogos"), (-1, "Voltar"), (0, "Sair"),
        ])

        match choice:
            case 1:
                add_game()
            case 2:
                list_games()
            case 0:
                print("Saíste do programa.")
                raise SystemExit
            case -1:
                return


def add_game():
    """Preenche um rascunho e guarda o jogo no estúdio escolhido."""
    temp_path = Path("data/temp.json")
    data_path = Path("data/data.json")

    while True:
        # Recupera os dados que ficaram guardados nas voltas anteriores do formulário.
        with temp_path.open(encoding="utf-8") as file:
            temp = json.load(file)

        # Cria a secção dos jogos se o ficheiro só tiver o rascunho dos estúdios.
        draft = temp.setdefault("game", {})

        with data_path.open(encoding="utf-8") as file:
            data = json.load(file)
        # Guarda o ID no rascunho para encontrar o estúdio mesmo que o nome mude.
        studio_id = draft.get("studio_id")
        studio = next(
            (entry for entry in data["studios"] if studio_id is not None and entry.get("id") == studio_id),
            None,
        )

        name = draft.get("name")
        genre = draft.get("genre")
        release_date = draft.get("release_date")
        copies_sold = draft.get("copies_sold")
        price = draft.get("price")

        # Os campos preenchidos aparecem no menu com o valor atual.
        studio_label = "Escolher estúdio"
        if studio:
            studio_label = f'Editar estúdio | {studio["name"]}'

        name_label = "Adicionar nome"
        if name:
            name_label = f"Editar nome | {name}"

        genre_label = "Adicionar género"
        if genre:
            genre_label = f"Editar género | {genre}"

        date_label = "Adicionar data de lançamento"
        if release_date:
            formatted_date = datetime.fromisoformat(release_date).strftime("%d-%m-%Y")
            date_label = f"Editar data de lançamento | {formatted_date}"

        copies_label = "Adicionar cópias vendidas"
        if copies_sold is not None:
            copies_label = f"Editar cópias vendidas | {copies_sold}"

        price_label = "Adicionar preço"
        if price is not None:
            price_label = f"Editar preço | {price}"

        options = [
            (1, studio_label),
            (2, name_label),
            (3, genre_label),
            (4, date_label),
            (5, copies_label),
            (6, price_label),
        ]

        # A confirmação aparece quando o estúdio existe e todos os campos estão preenchidos.
        # Zero também é válido para as cópias vendidas e para o preço.
        if studio and name and genre and release_date and copies_sold is not None and price is not None:
            options.append((7, "Adicionar jogo"))
        options.extend([(-1, "Voltar"), (0, "Sair")])

        choice = choose_menu("Adicionar jogo", options)

        match choice:
            case -1:
                return
            case 0:
                print("Saíste do programa.")
                raise SystemExit
            case 1:
                selected_id = list_studios(select=True)

                # Se voltar da lista sem escolher, mantém o estúdio do rascunho.
                if selected_id is None:
                    continue
                draft["studio_id"] = selected_id

            case 7:
                # Relê os dados antes de gravar para confirmar que o estúdio ainda existe.
                with data_path.open(encoding="utf-8") as file:
                    data = json.load(file)
                studio = next((entry for entry in data["studios"] if entry.get("id") == studio_id), None)

                if studio is None:
                    print("Estúdio não encontrado.")
                    time.sleep(3)
                    continue

                new_id = assign_game_ids(data)
                game = {
                    "id": new_id,
                    "name": name,
                    "genre": genre,
                    "release_date": release_date,
                    "copies_sold": copies_sold,
                    "price": price,
                }
                # Cada estúdio tem a sua própria lista de jogos no ficheiro.
                studio.setdefault("games", []).append(game)

                # Reescreve o ficheiro com o novo jogo e os restantes dados.
                with data_path.open("w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                # Depois de guardar, o formulário volta a ficar vazio.
                temp["game"] = {}
            case _:
                if not edit_game_field(draft, choice):
                    continue

        # Guarda o rascunho para o poder retomar depois de voltar ao submenu.
        with temp_path.open("w", encoding="utf-8") as file:
            json.dump(temp, file, ensure_ascii=False, indent=4)

        if choice == 7:
            print(f"Jogo adicionado a {studio['name']} com sucesso!")
            time.sleep(3)


def edit_game_field(draft, choice):
    """Pede e valida um campo do formulário do jogo."""
    # A criação e a edição usam as mesmas opções e validações.
    match choice:
        case 2:
            # strip() remove espaços nas extremidades. Enter mantém o nome atual.
            draft["name"] = input("Nome (Enter para manter): ").strip() or draft.get("name")

        case 3:
            # Aplica ao género o mesmo comportamento de edição do nome.
            draft["genre"] = input("Género (Enter para manter): ").strip() or draft.get("genre")

        case 4:
            value = input("Data de lançamento (DD-MM-AAAA, Enter para manter): ").strip()

            # Uma entrada vazia mantém a data atual e volta ao formulário.
            if not value:
                return False

            # Mostra a data como DD-MM-AAAA e guarda-a como AAAA-MM-DD.
            try:
                draft["release_date"] = datetime.strptime(value, "%d-%m-%Y").date().isoformat()
            except ValueError:
                print("Introduz uma data válida no formato DD-MM-AAAA.")
                time.sleep(3)
                return False

        case 5:
            value = input("Cópias vendidas (Enter para manter): ").strip()

            if not value:
                return False

            try:
                copies = int(value)

                # As cópias vendidas são um número inteiro. Zero é um valor válido.
                if copies < 0:
                    raise ValueError
                draft["copies_sold"] = copies
            except ValueError:
                print("Introduz um número inteiro maior ou igual a zero.")
                time.sleep(3)
                return False

        case 6:
            value = input("Preço (Enter para manter): ").strip()

            if not value:
                return False

            try:
                # Aceita vírgula ou ponto como separador decimal.
                amount = float(value.replace(",", "."))

                if not math.isfinite(amount) or amount < 0:
                    raise ValueError
                draft["price"] = amount
            except ValueError:
                print("Introduz um preço válido maior ou igual a zero.")
                time.sleep(3)
                return False
    return True


def assign_game_ids(data):
    """Preenche os IDs em falta e devolve o próximo ID disponível."""
    next_id = 1

    # Procura o maior ID entre os jogos de todos os estúdios.
    for studio in data["studios"]:
        for game in studio.get("games", []):
            game_id = game.get("id")

            if game_id is not None and game_id >= next_id:
                next_id = game_id + 1

    # Os jogos antigos recebem um ID a seguir aos que já existem.
    for studio in data["studios"]:
        for game in studio.get("games", []):
            if game.get("id") is None:
                game["id"] = next_id
                next_id += 1

    return next_id


def list_games():
    """Lista os jogos do estúdio escolhido."""
    studio_id = list_studios(select=True)

    if studio_id is None:
        return

    data_path = Path("data/data.json")

    # Relê a lista para mostrar logo o resultado de uma edição ou eliminação.
    while True:
        with data_path.open(encoding="utf-8") as file:
            data = json.load(file)
        studio = next((entry for entry in data["studios"] if entry.get("id") == studio_id), None)

        if studio is None:
            print("Estúdio não encontrado.")
            time.sleep(3)
            return

        games = studio.get("games", [])

        # Guarda os IDs dos jogos antigos antes de os usar no menu.
        if any(game.get("id") is None for game in games):
            assign_game_ids(data)

            with data_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        options = []

        for game in games:
            game_id = game["id"]
            release_date = datetime.fromisoformat(game["release_date"]).strftime("%d-%m-%Y")
            label = (f"ID {game_id} | {game['name']} | {game['genre']} | {release_date} | "
                     f"{game['copies_sold']} cópias | {game['price']:.2f}")
            options.append((game_id, label))

        options.extend([(-1, "Voltar"), (0, "Sair")])

        notes = []

        if not games:
            notes.append("Este estúdio ainda não tem jogos.")

        choice = choose_menu(f"Jogos de {studio['name']}", options, notes=notes)

        match choice:
            case -1:
                return
            case 0:
                print("Saíste do programa.")
                raise SystemExit
            case _:
                game = next(game for game in games if game["id"] == choice)
                edit_game(studio_id, game)


def edit_game(studio_id, game):
    """Edita uma cópia do jogo até o utilizador guardar."""
    # Edita uma cópia em memória para poder descartar as mudanças ao voltar.
    draft = game.copy()

    while True:
        release_date = datetime.fromisoformat(draft["release_date"]).strftime("%d-%m-%Y")
        options = [
            (2, f"Editar nome | {draft['name']}"),
            (3, f"Editar género | {draft['genre']}"),
            (4, f"Editar data de lançamento | {release_date}"),
            (5, f"Editar cópias vendidas | {draft['copies_sold']}"),
            (6, f"Editar preço | {draft['price']}"),
            (7, "Guardar alterações"),
            (8, "Eliminar jogo"),
            (-1, "Voltar"),
            (0, "Sair"),
        ]
        choice = choose_menu("Editar jogo", options)

        match choice:
            case 7:
                if save_game_changes(studio_id, game, draft):
                    print("Alterações guardadas com sucesso!")
                    time.sleep(3)
                    return
            case 8:
                # Se a eliminação for concluída, volta à lista para a atualizar.
                if delete_game(studio_id, game):
                    return
            case -1:
                return
            case 0:
                print("Saíste do programa.")
                raise SystemExit
            case _:
                edit_game_field(draft, choice)


def delete_game(studio_id, game):
    """Elimina o jogo depois de confirmar o seu nome."""
    while True:
        choice = choose_menu(f'Eliminar jogo "{game["name"]}"', [
            (-1, "Voltar"), (1, "Confirmar eliminação"), (0, "Sair"),
        ])

        if choice == -1:
            return False

        if choice == 0:
            print("Saíste do programa.")
            raise SystemExit

        # Pede o nome guardado, mesmo que haja um nome diferente no rascunho.
        name = input("Introduz o nome do jogo para confirmar a eliminação: ").strip()

        if name != game["name"]:
            print("Nome do jogo incorreto.")
            time.sleep(3)
            continue

        if save_game_changes(studio_id, game, None):
            print("Jogo eliminado com sucesso!")
            time.sleep(3)
            return True
        return False


def save_game_changes(studio_id, game, draft):
    """Grava a edição ou a eliminação se o jogo ainda corresponder à seleção."""
    data_path = Path("data/data.json")

    try:
        # Relê o ficheiro para preservar os restantes jogos e estúdios.
        with data_path.open(encoding="utf-8") as file:
            data = json.load(file)
        studio = next((entry for entry in data["studios"] if entry.get("id") == studio_id), None)
        games = []

        if studio is not None:
            games = studio.get("games", [])

        # O ID permite encontrar o jogo mesmo que a posição na lista mude.
        current_game = next((entry for entry in games if entry.get("id") == game["id"]), None)

        if current_game is None or current_game != game:
            print("O jogo foi alterado ou já não existe. Volta à lista de jogos.")
            time.sleep(3)
            return False

        # A eliminação remove o jogo e a edição aplica os valores do rascunho.
        if draft is None:
            games.remove(current_game)
        else:
            current_game.update(draft)

        with data_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except (OSError, ValueError) as error:
        print(f"Não foi possível guardar as alterações: {error}")
        time.sleep(3)
        return False

    return True
