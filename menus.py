# importes internos
import sys
import os

# importes de ficheiros
import estudios
import jogos
import dlcs

def menu_gerir_estudios():
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = int(input("================================================\n                 INSERT COIN\n================================================\n                   ESTUDIOS\n================================================\n"))

def menu_gerir_jogos():
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = int(input("================================================\n                 INSERT COIN\n================================================\n                     JOGOS\n================================================\n"))

def menu_gerir_dlcs():
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = int(input("================================================\n                 INSERT COIN\n================================================\n                      DLCS\n================================================\n"))

def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = int(input("================================================\n                 INSERT COIN\n================================================\n1. Gerir estúdios\n2. Gerir jogos\n3. Gerir DLC\n4. Pesquisar catálogo\n5. Relatórios financeiros [protegido]\n6. Gráficos\n7. Histórico de ações\n8. Anular última alteração\n0. Sair\n================================================\nEscolha uma opção: "))
    
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
            sys.exit()