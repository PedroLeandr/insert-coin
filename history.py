import json


def ler_historico():
    """Lê e devolve a lista de ações guardadas no ficheiro de histórico."""
    try:
        # Abre o ficheiro em modo de leitura com suporte para acentos (UTF-8).
        ficheiro = open("data/history.json", "r", encoding="utf-8")
        historico = json.load(ficheiro)
        ficheiro.close()
        return historico
    except FileNotFoundError:
        # Se o ficheiro ainda não existir, inicia com uma lista vazia.
        return []


def guardar_historico(historico):
    """Guarda a lista atualizada de ações no ficheiro de histórico."""
    # Abre o ficheiro em modo de escrita e grava os dados formatados.
    ficheiro = open("data/history.json", "w", encoding="utf-8")
    json.dump(historico, ficheiro, ensure_ascii=False, indent=4)
    ficheiro.close()


def registar_acao(descricao, dados_antigos):
    """Regista uma ação e guarda uma cópia dos dados anteriores à alteração."""
    historico = ler_historico()

    # Cria um registo com a descrição da operação e o estado anterior completo.
    entrada = {"acao": descricao, "estado_anterior": dados_antigos}

    # Adiciona o novo registo ao topo da lista (pilha de histórico) e grava no disco.
    historico.append(entrada)
    guardar_historico(historico)


def anular_ultima_acao():
    """Anula a última ação realizada e repõe os dados ao estado anterior."""
    historico = ler_historico()

    # Verifica se existem registos disponíveis para anular.
    if len(historico) == 0:
        print("Não há ações para anular.")
        return

    # Remove e obtém o registo mais recente do histórico.
    ultima_entrada = historico.pop()

    # Sobrescreve o ficheiro principal com os dados anteriores à ação.
    ficheiro_dados = open("data/data.json", "w", encoding="utf-8")
    json.dump(
        ultima_entrada["estado_anterior"],
        ficheiro_dados,
        ensure_ascii=False,
        indent=4,
    )
    ficheiro_dados.close()

    # Atualiza o ficheiro de histórico sem a ação que acabou de ser anulada.
    guardar_historico(historico)
    print("Ação anulada com sucesso:", ultima_entrada["acao"])

import json
import time
from menu_display import choose_menu

# ... (mantém aqui as tuas funções ler_historico, guardar_historico, registar_acao e anular_ultima_acao) ...

def menu_history():
    """Apresenta o histórico de ações realizadas e permite anular a última."""
    while True:
        historico = ler_historico()
        notas = []

        if len(historico) == 0:
            notas.append("Ainda não existem ações registadas no histórico.")
        else:
            notas.append("Histórico de ações (mais recente em baixo):")
            for indice, registo in enumerate(historico, start=1):
                notas.append(f"  {indice}. {registo['acao']}")

        opcoes = []
        if len(historico) > 0:
            opcoes.append((1, f"Anular última ação ({historico[-1]['acao']})"))
        opcoes.extend([(-1, "Voltar"), (0, "Sair")])

        escolha = choose_menu("Histórico e Anular", opcoes, notes=notas)

        match escolha:
            case 1:
                anular_ultima_acao()
            case -1:
                return
            case 0:
                print("Saíste do programa.")
                raise SystemExit