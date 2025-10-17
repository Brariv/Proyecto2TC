
def grammar_parsing(grammar: dict[str, list[str]]) -> dict[str, list[list[str]]]:
    cnf = {}
    new_var_count = 1
    terminal_map = {}

    # Step 1: Convert terminals to non-terminals
    for head, productions in grammar.items():
        cnf.setdefault(head, [])
        for prod in productions:
            symbols = prod.split()
            for i, sym in enumerate(symbols):
                if sym.islower():  # treat lowercase as terminal
                    if sym not in terminal_map:
                        term_var = f"T_{sym}"
                        terminal_map[sym] = term_var
                        cnf[term_var] = [[sym]]  # T_sym -> sym
                    symbols[i] = terminal_map[sym]

            # Step 2: Split long productions
            while len(symbols) > 2:
                new_var = f"X{new_var_count}"
                new_var_count += 1
                cnf[new_var] = [symbols[:2]]
                symbols = [new_var] + symbols[2:]

            cnf[head].append(symbols)

    # Step 3: Eliminate unit productions (A → B)
    changed = True
    while changed:
        changed = False
        for head in list(cnf.keys()):
            new_productions = []
            to_remove = []
            for prod in cnf[head]:
                if len(prod) == 1 and prod[0] in cnf:  # unit production
                    to_remove.append(prod)
                    for sub_prod in cnf[prod[0]]:
                        if sub_prod not in cnf[head]:
                            new_productions.append(sub_prod)
                    changed = True
            # Remove unit productions
            for prod in to_remove:
                cnf[head].remove(prod)
            # Add expanded productions
            cnf[head].extend(new_productions)

    print("\n=== CNF Parsed Grammar (unit productions eliminated) ===")
    for k, v in cnf.items():
        print(f"{k} → {v}")

    return cnf



