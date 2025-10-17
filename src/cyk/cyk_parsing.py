# Function to perform the CYK Algorithm
def cyk_parse(word: str, cnf: dict[str, list[list[str]]]) -> bool:
    n = len(word)
    T = [[set() for _ in range(n)] for _ in range(n)]

    # Build a reverse map: which non-terminals produce each terminal
    terminal_rules = {}
    for head, prods in cnf.items():
        for prod in prods:
            if len(prod) == 1 and prod[0].islower():
                if prod[0] not in terminal_rules:
                    terminal_rules[prod[0]] = set()
                terminal_rules[prod[0]].add(head)

    # Fill in length-1 substrings
    for i, w in enumerate(word):
        if w in terminal_rules:
            T[i][i].update(terminal_rules[w])

    # CYK algorithm for substrings length >= 2
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                left_cell = T[i][k]
                right_cell = T[k + 1][j]
                for head, prods in cnf.items():
                    for prod in prods:
                        if len(prod) == 2 and prod[0] in left_cell and prod[1] in right_cell:
                            T[i][j].add(head)

    # The word is accepted if the start symbol is in T[0][n-1]
    return 'S' in T[0][n-1]

