def print_menu(title, *sections):
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
    for section in sections:
        print(*section, sep="\n")
        print(separator)
