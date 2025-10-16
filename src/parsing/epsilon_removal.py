def removeEpsilonProductions(grammar: dict[str, list[str]]) -> dict[str, list[str]]:
    print("=== Given Grammar ===")
    for head, prods in grammar.items():
        print(f"{head} → {' | '.join(prods)}")

    # find nullable symbols
    nullable = set()
    changed = True
    while changed:
        changed = False
        for head, prods in grammar.items():
            for p in prods:
                if p == "𝜀" or all(ch in nullable for ch in p):
                    if head not in nullable: # if we haven't already put the production in the nullable
                        nullable.add(head)
                        changed = True

    print("\n=== Nullable Symbols ===")
    print(nullable)

    # generate new productions
    newG = {head: set() for head in grammar}
    for head, prods in grammar.items():
        for p in prods:
            if p == "𝜀":
                continue
            # find nullable positions
            positions = []
            for i, ch in enumerate(p):
                if ch in nullable:
                    positions.append(i)

            # manually generate subsets of positions
            subsets = [[]]
            for pos in positions:
                new_subsets = []
                for subset in subsets:
                    new_subsets.append(subset)          # keep original
                    new_subsets.append(subset + [pos])  # add this position
                subsets = new_subsets

            # build candidates
            for subset in subsets:
                s = ""
                for i, ch in enumerate(p):
                    if i not in subset:
                        s += ch
                if s == "":
                    s = "𝜀"
                print(f"Generated from {p}: {s}")
                newG[head].add(s)

    # remove epsilon if not from start
    start = list(grammar.keys())[0]
    for head in newG:
        if "𝜀" in newG[head]:
            newG[head].remove("𝜀")

    print("\n=== Resulting Grammar ===")
    for k, v in newG.items():
        print(f"{k} → {' | '.join(sorted(v))}")

    return {k: sorted(v) for k, v in newG.items()}
