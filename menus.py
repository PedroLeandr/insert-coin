# importes internos
import sys
import os

# importes de ficheiros
import estudios
import jogos
import dlcs

def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = int(input(
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
        "Escolha uma opção: "))
    
    match escolha:
        case 1:
            estudios.gerir_estudios()
        case 2:
            jogos.gerir_jogos()
        case 3:
            dlcs.gerir_dlcs()
        case 4:
            pesquisar_catalogo()
        case 5:
            relatorio_financeiro()
        case 6:
            graficos()
        case 7:
            historico_de_acoes()
        case 8:
            anular_ultima_alteracao()
        case 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

def menu_gerir_estudios():
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = int(input(
        "================================================\n"
        "                 INSERT COIN\n"
        "================================================\n"
        "                   ESTUDIOS\n"
        "================================================\n"
        "-1. Voltar\n"
        "0. Sair\n"
        "================================================\n"
        "Escolha uma opção: "))

    match escolha:
        case -1:
            menu_principal()
        case 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

def menu_gerir_jogos():
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = int(input(
        "================================================\n"
        "                 INSERT COIN\n"
        "================================================\n"
        "                     JOGOS\n"
        "================================================\n"
        "-1. Voltar\n"
        "0. Sair\n"
        "================================================\n"
        "Escolha uma opção: "))

    match escolha:
        case -1:
            menu_principal()
        case 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

def menu_gerir_dlcs():
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = int(input(
        "================================================\n"
        "                 INSERT COIN\n"
        "================================================\n"
        "                      DLCS\n"
        "================================================\n"
        "-1. Voltar\n"
        "0. Sair\n"
        "================================================\n"
        "Escolha uma opção: "))

    match escolha:
        case -1:
            menu_principal()
        case 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
