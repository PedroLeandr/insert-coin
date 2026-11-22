import os
import sys

# Estas bibliotecas dão acesso ao teclado e às cores da consola no Windows.
if os.name == "nt":
    import ctypes
    import msvcrt


def choose_menu(title, options, *, heading=None, notes=()):
    """Apresenta pares (valor, texto) e devolve o valor escolhido."""
    selected = 0
    # As setas precisam de um terminal interativo no Windows.
    use_arrows = os.name == "nt" and sys.stdin.isatty() and sys.stdout.isatty()
    use_color = False

    if use_arrows:
        # Ativa as cores ANSI na consola do Windows, se estiverem disponíveis.
        console = ctypes.windll.kernel32
        handle = ctypes.c_void_p(msvcrt.get_osfhandle(sys.stdout.fileno()))
        mode = ctypes.c_ulong()

        if console.GetConsoleMode(handle, ctypes.byref(mode)):
            use_color = bool(console.SetConsoleMode(handle, mode.value | 0x0004))

    while True:
        if use_arrows:
            os.system("cls")

        rows = []
        if heading:
            rows.append(f"  {heading}")

        for index, (value, label) in enumerate(options):
            if use_arrows:
                marker = " "

                if index == selected:
                    marker = ">"

                rows.append(f"{marker} {label}")
            elif heading and value > 0:
                rows.append(f"  {label}")
            else:
                rows.append(f"{value}. {label}")

        controls = "Introduz o número da opção."
        if use_arrows:
            controls = "↑/↓ Mover | Enter Selecionar"

        # Conta a linha do cabeçalho ao calcular a posição do fundo azul.
        selected_row = None
        if use_color:
            selected_row = selected

            if heading:
                selected_row += 1

        print_menu(title, rows, [*notes, controls], selected_row=selected_row)

        # Nos outros ambientes, a opção é escolhida pelo número.
        if not use_arrows:
            entered = input("Opção: ").strip()

            for value, _ in options:
                if entered == str(value):
                    return value

            print("Opção inválida.")
            continue

        while True:
            key = msvcrt.getwch()

            if key == "\r":
                return options[selected][0]

            # No Windows, as setas são lidas em dois passos.
            if key in ("\x00", "\xe0"):
                arrow = msvcrt.getwch()

                # O resto da divisão permite passar da primeira opção para a última e vice-versa.
                if arrow == "H":
                    selected = (selected - 1) % len(options)
                    break
                if arrow == "P":
                    selected = (selected + 1) % len(options)
                    break


def print_menu(title, *sections, selected_row=None):
    """Centra os títulos e adapta os separadores às linhas do menu."""
    headings = ["Insert Coin"]
    if title:
        headings.append(title)

    # Reserva dez caracteres além da linha mais comprida, incluindo os títulos.
    width = max(
        len(line)
        for section in (headings, *sections)
        for line in section
    ) + 10
    separator = "=" * width

    print(separator)
    for heading in headings:

        print(heading.center(width))
        print(separator)

    # Cada grupo de linhas termina com o mesmo separador.
    for section_index, section in enumerate(sections):
        for row_index, line in enumerate(section):
            # Aplica a cor depois de calcular a largura e repõe a cor no fim da linha.
            if section_index == 0 and row_index == selected_row:
                print(f"\033[44;97m{line.ljust(width)}\033[0m")
            else:
                print(line)
        print(separator)
