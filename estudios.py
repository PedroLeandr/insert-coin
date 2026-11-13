import json
import os
import time
import sys

import menus

# import de dados "temporarios"
from dados import ler_temp

temp = ler_temp()


def menu_gerir_estudios():
    temp = ler_temp()
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = input(
        "================================================\n"
        "                 INSERT COIN\n"
        "================================================\n"
        "                   ESTUDIOS\n"
        "================================================\n"
        "1. Adicionar Estudio\n"
        "2. Editar Estudio\n"
        "-1. Voltar\n"
        "0. Sair\n"
        "================================================\n"
        "Escolha uma opção: ")

    match escolha:
        case "1":
            adicionar_estudio()
        case "2":
            menu_editar_estudio()
        case "-1":
            menu_principal()
        case "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(escolha, "Não é uma opção válida!")
            time.sleep(3)
            menu_gerir_estudios()

def adicionar_estudio():
    temp = ler_temp()
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = temp["estudio"]["nome"]
    pais = temp["estudio"]["pais"]
    comissao = temp["estudio"]["comissao"]

    escolha = input(
        "================================================\n"
        "                 INSERT COIN\n"
        "================================================\n"
        "              ADICIONAR ESTUDIO\n"
        "================================================\n"
        f"1. {f'Alterar Nome | {nome}' if nome else 'Adicionar Nome'}\n"
        f"2. {f'Alterar País | {pais}' if pais else 'Adicionar País'}\n"
        f"3. {f'Alterar Comissão | {comissao}%' if comissao else 'Adicionar Comissão'}\n"
        f"{'4. Adicionar Estúdio' + chr(10) if nome and pais and comissao is not None else ''}"
        "-1. Voltar\n"
        "0. Sair\n"
        "================================================\n"
        "Escolha uma opção: ")

    match escolha:
        case "":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(escolha, "Não é uma opção válida!")
            time.sleep(3)
            adicionar_estudio()
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
                        with open("data/temp.json", "w", encoding="utf-8") as arquivo:
                            json.dump(temp, arquivo, indent=4, ensure_ascii=False)

                        break

                    print("A comissão deve estar entre 0 e 100!")

                except ValueError:
                    print("Introduz um número válido!")

        case "4":
            if nome and pais and comissao is not None:
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
                menu_gerir_estudios()

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(escolha, "Não é uma opção válida!")
                time.sleep(3)
                adicionar_estudio()

        case "-1":
            menu_gerir_estudios()

        case "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(escolha, "Não é uma opção válida!")
            time.sleep(3)
            adicionar_estudio()


def gerir_estudios():
    menu_gerir_estudios()


    adicionar_estudio()
    