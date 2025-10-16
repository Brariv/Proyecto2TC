def grammar_parsing(Grammar_Array: dict[str, list[str]]) -> dict[str, list[list[str]]]:
    R = {}

    for i in range(len(Grammar_Array)):

        Rule = []
        SubRule = []
        key = list(Grammar_Array.keys())[i]
        rule_items = Grammar_Array[key]
        for j in range(len(rule_items)):
            item = rule_items[j].split(" ")
            if len(item) > 1:
                if len(SubRule) > 0:
                    Rule.append(SubRule)
                    SubRule = []
                SubRule.append(item[0])
                SubRule.append(item[1])
            else:
                if len(SubRule) > 0:
                    Rule.append(SubRule)

                SubRule = []
                SubRule.append(rule_items[j])
                Rule.append(SubRule)
                SubRule = []

            if j == len(rule_items) - 1 and len(SubRule) > 0:
                Rule.append(SubRule)
                SubRule = []
        
        R[key] = Rule

    print("\n=== CNF Parsed Grammar ===")
    for k, v in R.items():
        print(f"{k} → {v}")

    return R


