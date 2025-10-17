

def grammar_parsing(grammar: dict[str, list[str]]) -> dict[str, list[list[str]]]:
    cnf = {}
    new_var_count = 1
    terminal_map = {}

    # Step 1: Convert terminals to non-terminals
    for head, productions in grammar.items():
        cnf.setdefault(head, [])
        for prod in productions:
            symbols = prod.split()
            new_symbols = []
            for sym in symbols:
                if sym.islower():  # terminal
                    if sym not in terminal_map:
                        term_var = f"T_{sym}"
                        terminal_map[sym] = term_var
                        cnf[term_var] = [[sym]]  # T_sym -> sym
                    new_symbols.append(terminal_map[sym])
                else:
                    new_symbols.append(sym)
            symbols = new_symbols

            # Step 2: Split productions >2 symbols
            while len(symbols) > 2:
                new_var = f"X{new_var_count}"
                new_var_count += 1
                cnf[new_var] = [symbols[:2]]
                symbols = [new_var] + symbols[2:]

            cnf[head].append(symbols)

    print("\n=== CNF Parsed Grammar (minimal, no direct terminals) ===")
    for k, v in cnf.items():
        print(f"{k} → {v}")

    return cnf

