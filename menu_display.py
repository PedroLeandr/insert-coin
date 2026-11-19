def print_menu(title, *sections):
    """Centra os títulos e adapta os separadores às linhas do menu."""
    headings = ["Insert Coin"]
    if title:
        headings.append(title)

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

    for section in sections:
        print(*section, sep="\n")
        print(separator)
