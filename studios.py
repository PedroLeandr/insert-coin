import os
import time
import json

def menu_studios():
    """Apresenta as operações disponíveis para os estúdios."""
    # Mantém o submenu aberto depois de cada operação.
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            "============================\n"
            f"{'Insert Coin':^28}\n"
            "============================\n"
            f"{'Estudios':^28}\n"
            "============================\n"
            "1. Adicionar\n"
            "-1. Voltar\n"
            "0. Sair\n"
            "============================\n"
            )
        try: 
            choice = int(input("Opção: "))

            match choice:
                case 1: 
                    add_studio()
                
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
        # ^28 centra os títulos numa largura de 28 caracteres.
        print(
            "============================\n"
            f"{'Insert Coin':^28}\n"
            "============================\n"
            f"{'Adicionar Estudio':^28}\n"
            "============================\n"
            f"1. {'Adicionar Nome' if name is None else 'Editar Nome | ' + name}: \n"
            f"2. {'Adicionar País' if country is None else 'Editar País | ' + country}: \n"
            f"3. {'Adicionar Comissão' if commission is None else 'Editar Comissão | ' + str(commission) + "%"}: \n"
            f"{'4. Adicionar Estudio\n' if name is not None and country is not None and commission is not None else ''}"
            "-1. Voltar\n"
            "0. Sair\n"
            "============================\n"
            )
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
