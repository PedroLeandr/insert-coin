# importes internos
import sys
import os
import time

# importes de ficheiros
import estudios
import jogos
import dlcs

# import de dados "temporarios"
from dados import ler_temp

def menu_principal():
    temp = ler_temp()
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = input(
        "================================================\n"
        "                 INSERT COIN\n"
        "================================================\n"
        "1. Gerir estúdios\n"
        "2. Gerir jogos\n"
        "3. Gerir DLC\n"
        "4. Pesquisar catálogo\n"
        "5. Relatórios financeiros [protegido]\n"
        "6. Gráficos\n"
        "7. Histórico de ações\n"
        "8. Anular última alteração\n"
        "0. Sair\n"
        "================================================\n"
        "Escolha uma opção: ")
    
    match escolha:
        case "1":
            estudios.gerir_estudios()
        case "2":
            jogos.gerir_jogos()
        case "3":
            dlcs.gerir_dlcs()
        case "4":
            pesquisar_catalogo()
        case "5":
            relatorio_financeiro()
        case "6":
            graficos()
        case "7":
            historico_de_acoes()
        case "8":
            anular_ultima_alteracao()
        case "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(escolha, "Não é uma opção válida!")
            time.sleep(3)
            menu_principal()


# ESTUDIOS

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
        "-1. Voltar\n"
        "0. Sair\n"
        "================================================\n"
        "Escolha uma opção: ")

    match escolha:
        case "1":
            menu_adicionar_estudio()
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

def menu_adicionar_estudio():
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
            menu_adicionar_estudio()
        case "1":
            estudios.adicionar_estudio(escolha)
        case "2":
            estudios.adicionar_estudio(escolha)
        case "3":
            estudios.adicionar_estudio(escolha)
        case "4":
            if nome and pais and comissao is not None:
                return estudios.adicionar_estudio(escolha)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(escolha, "Não é uma opção válida!")
                time.sleep(3)
                menu_adicionar_estudio()
        case "-1":
            menu_gerir_estudios()
        case "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(escolha, "Não é uma opção válida!")
            time.sleep(3)
            menu_adicionar_estudio()

# JOGOS

def menu_gerir_jogos():
    temp = ler_temp()
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = input(
        "================================================\n"
        "                 INSERT COIN\n"
        "================================================\n"
        "                     JOGOS\n"
        "================================================\n"
        "-1. Voltar\n"
        "0. Sair\n"
        "================================================\n"
        "Escolha uma opção: ")

    match escolha:
        case "":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(escolha, "Não é uma opção válida!")
            time.sleep(3)
            menu_gerir_jogos()
        case "-1":
            menu_principal()
        case "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(escolha, "Não é uma opção válida!")
            time.sleep(3)
            menu_gerir_jogos()

def menu_gerir_dlcs():
    temp = ler_temp()
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = input(
        "================================================\n"
        "                 INSERT COIN\n"
        "================================================\n"
        "                      DLCS\n"
        "================================================\n"
        "-1. Voltar\n"
        "0. Sair\n"
        "================================================\n"
        "Escolha uma opção: ")

    match escolha:
        case "-1":
            menu_principal()
        case "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(escolha, "Não é uma opção válida!")
            time.sleep(3)
            menu_gerir_dlcs()
