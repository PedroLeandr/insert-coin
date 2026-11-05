import json
import os
import time

import menus

# import de dados "temporarios"
from dados import ler_temp

temp = ler_temp()

def gerir_estudios():
    menus.menu_gerir_estudios()

def adicionar_estudio(escolha):
    match escolha:
        case "1":
            temp["estudio"]["nome"]  = input("Digite o nome do estudio: ")

            with open("data/temp.json", "w", encoding="utf-8") as arquivo:
                json.dump(temp, arquivo, indent=4, ensure_ascii=False)

        case "2":
            temp["estudio"]["pais"]  = input("Digite o país do estudio: ")

            with open("data/temp.json", "w", encoding="utf-8") as arquivo:
                json.dump(temp, arquivo, indent=4, ensure_ascii=False)
        
        case "3":
            while True:
                comissao = input("Digite a comissão: ").strip()
                comissao = comissao.removesuffix("%").strip()

                try:
                    comissao = float(comissao)

                    if 0 <= comissao <= 100:
                        temp["estudio"]["comissao"] = comissao
                        break

                    print("A comissão deve estar entre 0 e 100!")

                except ValueError:
                    print("Introduz um número válido!")

        case "4":
            estudio = temp["estudio"]

            with open("data/dados.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            
            novo_id = max(
                (e["id"] for e in dados["estudios"]),
                default=0
            ) + 1

            novo_estudio = {
                "id": novo_id,
                "nome": estudio["nome"],
                "pais": estudio["pais"],
                "comissao": estudio["comissao"],
                "jogos": []
            }

            dados["estudios"].append(novo_estudio)

            with open("data/dados.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)

            temp["estudio"] = {
                "nome": None,
                "pais": None,
                "comissao": None
            }

            with open("data/temp.json", "w", encoding="utf-8") as arquivo:
                json.dump(temp, arquivo, indent=4, ensure_ascii=False)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estudio adicionado com sucesso!")
            time.sleep(3)
            menus.menu_gerir_estudios()

    menus.menu_adicionar_estudio()
    