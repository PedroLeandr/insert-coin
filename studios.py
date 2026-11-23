import os
import time
import json
from pathlib import Path

from history import registar_acao
from menu_display import choose_menu

def menu_studios():
    """Apresenta as operações disponíveis para os estúdios."""
    # Volta a mostrar o submenu quando termina uma operação.
    while True:
        choice = choose_menu("Estúdios", [
            (1, "Adicionar"), (2, "Listar estúdios"), (-1, "Voltar"), (0, "Sair"),
        ])

        match choice:
            case 1:
                add_studio()
            case 2:
                list_studios()
            case 0:
                print("Saíste do programa.")
                raise SystemExit
            case -1:
                return


def add_studio():
    """Preenche um rascunho e guarda o estúdio quando os campos estão completos."""
    while True:
        # Recupera o rascunho, incluindo alterações guardadas nas voltas anteriores.
        # O bloco with fecha o ficheiro automaticamente depois da leitura.
        with open("data/temp.json", "r", encoding="utf-8") as file:
            temp = json.load(file)

        # Campos vazios são apresentados como dados ainda por preencher.
        name = temp.get("studio", {}).get("name") or None
        country = temp.get("studio", {}).get("country") or None
        # Preserva 0 como comissão válida, convertendo apenas a string vazia em None.
        commission = temp.get("studio", {}).get("commission")

        if commission == "":
            commission = None

        # Mostra os valores atuais e disponibiliza a confirmação com todos preenchidos.
        name_label = "Adicionar nome:"
        if name is not None:
            name_label = f"Editar nome | {name}:"

        country_label = "Adicionar país:"
        if country is not None:
            country_label = f"Editar país | {country}:"

        commission_label = "Adicionar comissão:"
        if commission is not None:
            commission_label = f"Editar comissão | {commission}%:"

        options = [(1, name_label), (2, country_label), (3, commission_label)]

        if name is not None and country is not None and commission is not None:
            options.append((4, "Adicionar estúdio"))
        options.extend([(-1, "Voltar"), (0, "Sair")])
        choice = choose_menu("Adicionar estúdio", options)

        match choice:
            case 1:
                # strip() remove espaços nas extremidades. Enter mantém o nome atual.
                temp["studio"]["name"] = input("Introduz o nome do estúdio (Enter para manter): ").strip() or name

                # Guarda o rascunho para permitir retomá-lo depois de sair do formulário.
                # ensure_ascii=False mantém acentos legíveis e indent=4 formata o JSON.
                with open("data/temp.json", "w", encoding="utf-8") as file:
                    json.dump(temp, file, ensure_ascii=False, indent=4)

            case 2:
                # Aplica ao país o mesmo comportamento de edição do nome.
                temp["studio"]["country"] = input("Introduz o país do estúdio (Enter para manter): ").strip() or country

                with open("data/temp.json", "w", encoding="utf-8") as file:
                    json.dump(temp, file, ensure_ascii=False, indent=4)

            case 3:
                try:
                    temp_commission = input("Comissão (Enter para manter): ")

                    # Enter mantém a comissão já guardada no rascunho.
                    if temp_commission != "":

                        # Aceita entradas como 15%, 15,5 e 15.5.
                        temp_commission = float(temp_commission.replace("%", "").replace(",", ".").strip())

                        # Só atualiza o rascunho se a percentagem estiver no intervalo.
                        if 0 <= temp_commission <= 100:
                            temp["studio"]["commission"] = temp_commission

                            with open("data/temp.json", "w", encoding="utf-8") as file:
                                json.dump(temp, file, ensure_ascii=False, indent=4)

                        else:
                            print("A comissão deve estar entre 0 e 100%.")
                            time.sleep(3)

                except ValueError:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("Introduz um número.")
                    time.sleep(3)

            case 4:
                # Repete a verificação mesmo que a opção tenha sido ocultada no menu.
                if name is not None and country is not None and commission is not None:
                    with open("data/data.json", "r", encoding="utf-8") as file:
                        data = json.load(file)

                    # Usa o maior ID atual mais um. Uma lista vazia começa no ID 1.
                    # Registos antigos sem ID contribuem com o valor 0.
                    new_id = max(
                        (studio.get("id", 0) for studio in data["studios"]),
                        default=0
                    ) + 1

                    # Cria um dicionário separado, com o ID primeiro no JSON.
                    # Assim, limpar o rascunho depois não altera o estúdio adicionado.
                    new_studio = {"id": new_id}
                    new_studio.update(temp["studio"])

                    # Guarda o estado atual no histórico antes de adicionar o estúdio.
                    registar_acao(f"Adicionar estúdio: {new_studio['name']}", data)

                    data["studios"].append(new_studio)

                    # Reescreve a coleção completa, incluindo os estúdios anteriores.
                    with open("data/data.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)

                    # Limpa e grava o rascunho para começar um novo registo.
                    # None é escrito como null no JSON.
                    temp["studio"]["name"] = None
                    temp["studio"]["country"] = None
                    temp["studio"]["commission"] = None

                    with open("data/temp.json", "w", encoding="utf-8") as file:
                        json.dump(temp, file, ensure_ascii=False, indent=4)

                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("Estúdio adicionado com sucesso!")
                    time.sleep(3)
                else:
                    print("Preenche todos os campos para adicionar o estúdio.")
                    time.sleep(3)

            case 0:
                print("Saíste do programa.")
                raise SystemExit

            case -1:
                # Volta ao submenu de estúdios. O rascunho guardado permanece disponível.
                return


def list_studios(*, select=False):
    """Devolve o ID em modo de seleção ou permite editar estúdios."""
    # Relê os dados em cada volta para refletir edições e eliminações.
    while True:
        with open("data/data.json", encoding="utf-8") as file:
            data = json.load(file)

        studios = data["studios"]

        if select and not any(studio.get("id") is not None for studio in studios):
            print("Não há estúdios disponíveis para escolher.")
            time.sleep(3)
            return

        name_width = max([len("Nome")] + [len(studio["name"]) for studio in studios])
        heading = f"{'ID':>4} | {'Nome':<{name_width}} | {'Comissão':>9}"
        options = []
        notes = []

        for studio in studios:
            studio_id = studio.get("id")
            name = studio["name"]
            commission = f"{studio['commission']:g}%"

            # Os registos antigos sem ID aparecem na lista como notas.
            if studio_id is None:
                notes.append(f"Estúdio sem ID: {name} | {commission}")
            else:
                options.append((studio_id, f"{studio_id:>4} | {name:<{name_width}} | {commission:>9}"))

        options.extend([(-1, "Voltar"), (0, "Sair")])

        title = "Listar estúdios"

        if select:
            title = "Escolher estúdio"
        choice = choose_menu(title, options, heading=heading, notes=notes)

        if choice == 0:
            print("Saíste do programa.")
            raise SystemExit

        if choice == -1:
            return

        if select:
            # O menu de jogos usa este ID para localizar o estúdio escolhido.
            return choice
        edit_studio(choice)


def edit_studio(studio_id):
    """Edita o estúdio selecionado e grava apenas após confirmação."""
    data_path = Path("data/data.json")
    with data_path.open(encoding="utf-8") as file:
        data = json.load(file)

    # O ID identifica o estúdio mesmo quando a lista tem saltos na numeração.
    studio = next(
        (studio for studio in data["studios"] if studio.get("id") == studio_id),
        None,
    )

    if studio is None:
        print("Estúdio não encontrado.")
        time.sleep(3)
        return

    # Edita uma cópia em memória para poder descartar as mudanças ao voltar.
    draft = studio.copy()

    while True:
        name = draft["name"]
        country = draft["country"]
        commission = draft["commission"]
        # Usa o mesmo formato de percentagem que a tabela de estúdios.
        commission_label = "Por preencher"
        if commission is not None:
            commission_label = f"{commission:g}%"
        options = [
            (1, f"Editar nome | {name or 'Por preencher'}"),
            (2, f"Editar país | {country or 'Por preencher'}"),
            (3, f"Editar comissão | {commission_label}"),
            (4, "Guardar alterações"),
            (5, "Eliminar estúdio"),
            (-1, "Voltar"),
            (0, "Sair"),
        ]
        choice = choose_menu("Editar estúdio", options)

        match choice:
            case 1:
                # strip() remove espaços nas extremidades. Enter mantém o valor atual.
                draft["name"] = input("Nome (Enter para manter): ").strip() or name
            case 2:
                draft["country"] = input("País (Enter para manter): ").strip() or country
            case 3:
                value = input("Comissão (Enter para manter): ").strip()
                # Uma entrada vazia mantém a comissão atual e volta ao menu.
                if not value:
                    continue

                try:
                    # Aceita entradas como 15%, 15,5 e 15.5.
                    rate = float(value.removesuffix("%").replace(",", "."))
                except ValueError:
                    print("Introduz um número.")
                    time.sleep(3)
                    continue

                # Só atualiza o rascunho se a percentagem estiver no intervalo.
                if 0 <= rate <= 100:
                    draft["commission"] = rate
                else:
                    print("A comissão deve estar entre 0 e 100%.")
                    time.sleep(3)
            case 4:
                try:
                    # Relê o ficheiro para trabalhar com a versão mais recente dos dados.
                    with data_path.open("r", encoding="utf-8") as file:
                        data = json.load(file)

                    current_studio = next(
                        (entry for entry in data["studios"] if entry.get("id") == studio_id),
                        None,
                    )

                    if current_studio is None:
                        print("Estúdio não encontrado.")
                        time.sleep(3)
                        return

                    # Guarda o estado atual no histórico antes de editar o estúdio.
                    registar_acao(f"Editar estúdio: {current_studio['name']}", data)

                    # Aplica ao estúdio encontrado os campos que mudaram no rascunho.
                    for field in ("name", "country", "commission"):
                        if draft[field] != studio[field]:
                            current_studio[field] = draft[field]

                    # Reescreve a coleção completa, incluindo os restantes estúdios.
                    with data_path.open("w", encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                except (OSError, ValueError) as error:
                    print(f"Não foi possível guardar as alterações: {error}")
                    time.sleep(3)
                    continue

                print("Alterações guardadas com sucesso!")
                time.sleep(3)
                return

            case 5:
                # Se a eliminação for concluída, volta à lista para atualizar a listagem.
                if delete_studio(studio_id):
                    return
            case -1:
                # Volta à lista e descarta as alterações pendentes.
                return
            case 0:
                print("Saíste do programa.")
                raise SystemExit


def delete_studio(studio_id):
    """Elimina o estúdio selecionado após confirmação pelo nome."""
    data_path = Path("data/data.json")
    with data_path.open(encoding="utf-8") as file:
        data = json.load(file)

    # Usa o nome guardado para confirmar a eliminação do estúdio selecionado pelo ID.
    studio = next(
        (studio for studio in data["studios"] if studio.get("id") == studio_id),
        None,
    )

    if studio is None:
        print("Estúdio não encontrado.")
        time.sleep(3)
        return

    while True:
        choice = choose_menu(f'Eliminar estúdio "{studio["name"]}"', [
            (-1, "Voltar"), (1, "Confirmar eliminação"), (0, "Sair"),
        ])

        if choice == -1:
            return

        if choice == 0:
            print("Saíste do programa.")
            raise SystemExit

        res = input("Introduz o nome do estúdio para confirmar a eliminação: ").strip()

        if res == studio["name"]:
            try:
                # Relê o ficheiro para preservar alterações aos outros estúdios.
                with data_path.open("r", encoding="utf-8") as file:
                    data = json.load(file)

                current_studio = next(
                    (entry for entry in data["studios"] if entry.get("id") == studio_id),
                    None,
                )
                # A confirmação só vale se o registo ainda existir com o mesmo nome.
                if current_studio is None or current_studio["name"] != res:
                    print("O estúdio foi alterado ou já não existe.")
                    time.sleep(3)
                    return

                # Guarda o estado atual no histórico antes de eliminar o estúdio.
                registar_acao(f"Eliminar estúdio: {current_studio['name']}", data)

                # Remove apenas o registo encontrado e guarda a coleção atualizada.
                data["studios"].remove(current_studio)
                with data_path.open("w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
            except (OSError, ValueError) as error:
                print(f"Não foi possível eliminar o estúdio: {error}")
                time.sleep(3)
                # Mantém o menu aberto para permitir nova tentativa ou cancelamento.
                continue

            print("Estúdio eliminado com sucesso!")
            time.sleep(3)
            return True

        print("Opção inválida ou nome do estúdio incorreto.")
        time.sleep(3)