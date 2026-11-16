import os
import time
import json

def menu_studios():
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
                    raise SystemExit

                case -1: 
                    return
                
                case _:
                    print("404")
                    time.sleep(3)

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("deve inserir um numero!")
            time.sleep(3)

def add_studio():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        with open("data/temp.json", "r", encoding="utf-8") as file:
            temp = json.load(file)

        name = temp.get("studio", {}).get("name") or None
        country = temp.get("studio", {}).get("country") or None
        commission = temp.get("studio", {}).get("commission")
        if commission == "":
            commission = None

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
                    temp["studio"]["name"] = input("Insira o nome do Estudio (ENTER para manter): ").strip() or name
                    
                    with open("data/temp.json", "w", encoding="utf-8") as file:
                        json.dump(temp, file, ensure_ascii=False, indent=4)

                case 2: 
                    temp["studio"]["country"] = input("Insira o país do Estudio (ENTER para manter): ").strip() or country

                    with open("data/temp.json", "w", encoding="utf-8") as file:
                        json.dump(temp, file, ensure_ascii=False, indent=4)

                case 3: 
                    try:
                        temp_commission = input("Comissão (ENTER para manter): ")

                        if temp_commission != "":

                            temp_commission = float(temp_commission.replace("%", "").replace(",", ".").strip())
                            
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
                    if name is not None and country is not None and commission is not None:
                        with open("data/data.json", "r", encoding="utf-8") as file:
                            data = json.load(file)
                        
                        new_id = max(
                            (studio.get("id", 0) for studio in data["studios"]),
                            default=0
                        ) + 1

                        new_studio = {"id": new_id}
                        new_studio.update(temp["studio"])

                        data["studios"].append(new_studio)

                        with open("data/data.json", "w", encoding="utf-8") as file:
                            json.dump(data, file, ensure_ascii=False, indent=4)

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
                    return
                
                case _:
                    print("404")
                    time.sleep(3)
                
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("deve inserir um numero!")
            time.sleep(3)
