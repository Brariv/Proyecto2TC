
def stringToGramatic(unparsed: list[str]) -> dict[str, list[str]]:
    grammar: dict[str, list[str]] = {}
    for raw in unparsed:
        line = raw.strip()

        if '→' not in line:
            continue

        lhs, rhs = line.split('→', 1)
        lhs, rhs = lhs.strip(), rhs.strip()

        if not lhs:
            continue

        for p in rhs.split('|'):
            alt = p.strip()
            if alt == '' or alt.lower() == 'epsilon' or alt == 'ε':
                alt = 'ε'
            grammar.setdefault(lhs, [])
            if alt not in grammar[lhs]:
                grammar[lhs].append(alt)
    return grammar
