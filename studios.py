import os
import time
import json
from pathlib import Path

from menu_display import print_menu

def menu_studios():
    """Apresenta as operações disponíveis para os estúdios."""
    # Mantém o submenu aberto depois de cada operação.
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_menu(
            "Estudios",
            ["1. Adicionar", "2. Listar Estudios", "-1. Voltar", "0. Sair"],
        )
        try: 
            choice = int(input("Opção: "))

            match choice:
                case 1: 
                    add_studio()

                case 2:
                    list_studios()
                
                case 0: 
                    print("Saiste")
                    # Encerra a aplicação, incluindo os menus que chamaram esta função.
                    raise SystemExit

                case -1: 
                    # Devolve o controlo ao menu principal.
                    return
                
                case _:
                    print("404")
                    time.sleep(3)

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("deve inserir um numero!")
            time.sleep(3)

def add_studio():
    """Preenche um rascunho e guarda o estúdio quando os campos estão completos."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

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
        options = [
            f"1. {'Adicionar Nome' if name is None else 'Editar Nome | ' + name}:",
            f"2. {'Adicionar País' if country is None else 'Editar País | ' + country}:",
            f"3. {'Adicionar Comissão' if commission is None else f'Editar Comissão | {commission}%'}:",
        ]
        if name is not None and country is not None and commission is not None:
            options.append("4. Adicionar Estudio")
        options.extend(["-1. Voltar", "0. Sair"])
        print_menu("Adicionar Estudio", options)
        try: 
            choice = int(input("Opção: "))

            match choice:
                case 1: 
                    # strip() remove espaços nas extremidades. Enter mantém o nome atual.
                    temp["studio"]["name"] = input("Insira o nome do Estudio (ENTER para manter): ").strip() or name
                    
                    # Guarda o rascunho para permitir retomá-lo depois de sair do formulário.
                    # ensure_ascii=False mantém acentos legíveis e indent=4 formata o JSON.
                    with open("data/temp.json", "w", encoding="utf-8") as file:
                        json.dump(temp, file, ensure_ascii=False, indent=4)

                case 2: 
                    # Aplica ao país o mesmo comportamento de edição do nome.
                    temp["studio"]["country"] = input("Insira o país do Estudio (ENTER para manter): ").strip() or country

                    with open("data/temp.json", "w", encoding="utf-8") as file:
                        json.dump(temp, file, ensure_ascii=False, indent=4)

                case 3: 
                    try:
                        temp_commission = input("Comissão (ENTER para manter): ")

                        if temp_commission != "":

                            # Aceita entradas como 15%, 15,5 e 15.5.
                            temp_commission = float(temp_commission.replace("%", "").replace(",", ".").strip())
                            
                            # Só atualiza o rascunho se a percentagem estiver no intervalo.
                            if 0 <= temp_commission <= 100:
                                temp["studio"]["commission"] = temp_commission
                                
                                with open("data/temp.json", "w", encoding="utf-8") as file:
                                    json.dump(temp, file, ensure_ascii=False, indent=4)

                            else:
                                print("A comissao deve estar entre 0 e 100!")
                                time.sleep(3)
                    
                    except ValueError:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("deve inserir um numero!")
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

                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Estudio adicionado com sucesso!")
                        time.sleep(3)
                    else:
                        print("404")
                        time.sleep(3)
                
                case 0: 
                    print("Saiste")
                    raise SystemExit

                case -1: 
                    # Volta ao submenu de estúdios. O rascunho guardado permanece disponível.
                    return
                
                case _:
                    print("404")
                    time.sleep(3)
                
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("deve inserir um numero!")
            time.sleep(3)

def list_studios():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        with open("data/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        studios = data["studios"]

        largura_nome = max([len("Nome")] + [len(studio["name"]) for studio in studios])

        header = f"{'ID':>4} | {'Nome':<{largura_nome}} | {'Comissão':>9}"
        table = [header, "-" * len(header)]

        for studio in studios:
            id_estudio = studio.get("id", "-")
            nome = studio["name"]
            comissao = f"{studio['commission']:g}%"
            table.append(f"{id_estudio:>4} | {nome:<{largura_nome}} | {comissao:>9}")

        print_menu("Listar Estudios", table, ["\"Para editar um Estúdio insira o ID do Estúdio\"", "-1. Voltar", "0. Sair"])

        try:
            choice = int(input("Opção: "))

            match choice:
                case 0:
                    print("Saiste")
                    raise SystemExit

                case -1:
                    # Volta ao submenu de estúdios. O rascunho guardado permanece disponível.
                    return

                case _:
                    # Procura o ID introduzido antes de abrir o menu de edição.
                    for studio in studios:
                        if studio.get("id") == choice:
                            edit_studio(choice)
                            break
                    else:
                        print("Estúdio não encontrado.")
                        time.sleep(3)

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("deve inserir um numero!")
            time.sleep(3)

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

    # Mantém os valores originais para gravar apenas os campos alterados.
    draft = studio.copy()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        name = draft["name"]
        country = draft["country"]
        commission = draft["commission"]
        # Usa o mesmo formato de percentagem que a tabela de estúdios.
        commission_label = "Por preencher" if commission is None else f"{commission:g}%"
        options = [
            f"1. Editar Nome | {name or 'Por preencher'}",
            f"2. Editar País | {country or 'Por preencher'}",
            f"3. Editar Comissão | {commission_label}",
            "4. Guardar alterações",
            "-1. Voltar",
            "0. Sair",
        ]
        print_menu("Editar Estúdio", options)

        try:
            choice = int(input("Opção: "))
        except ValueError:
            print("Deve inserir um número!")
            time.sleep(3)
            continue

        match choice:
            case 1:
                # strip() remove espaços nas extremidades. Enter mantém o valor atual.
                draft["name"] = input("Nome (ENTER para manter): ").strip() or name
            case 2:
                draft["country"] = input("País (ENTER para manter): ").strip() or country
            case 3:
                value = input("Comissão (ENTER para manter): ").strip()
                if not value:
                    continue
                try:
                    # Aceita entradas como 15%, 15,5 e 15.5.
                    rate = float(value.removesuffix("%").replace(",", "."))
                except ValueError:
                    print("Deve inserir um número!")
                    time.sleep(3)
                    continue

                # Só atualiza o rascunho se a percentagem estiver no intervalo.
                if 0 <= rate <= 100:
                    draft["commission"] = rate
                else:
                    print("A comissão deve estar entre 0 e 100!")
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
            case -1:
                # Volta à lista e descarta as alterações pendentes.
                return
            case 0:
                print("Saíste")
                raise SystemExit
            case _:
                print("Opção inválida.")
                time.sleep(3)
