def grammar_parsing(Grammar_Array: dict[str, list[str]]) -> dict[str, list[list[str]]]:
    R = {}

    for i in range(len(Grammar_Array)):

        Rule = [] 
        SubRule = []
        key = list(Grammar_Array.keys())[i]
        rule_items = Grammar_Array[key]

        for j in range(len(rule_items)):
            item = rule_items[j].split(" ")
            if len(item) > 1: # if we have more than one item, we need to group them
                if len(SubRule) > 0: # if we already have something in the subrule, we need to save it first
                    Rule.append(SubRule)
                    SubRule = []
                SubRule.append(item[0])
                SubRule.append(item[1])
            else: # if we have just one item, we can just add it to the subrule because it an OR
                if len(SubRule) > 0: # if we already have something in the subrule, we need to save it first
                    Rule.append(SubRule)

                SubRule = []
                SubRule.append(rule_items[j])
                Rule.append(SubRule)
                SubRule = []

            if j == len(rule_items) - 1 and len(SubRule) > 0: # if we are at the end and we have something in the subrule, we need to save it
                Rule.append(SubRule)
                SubRule = []
        
        R[key] = Rule # finally we save the rule to the dictionary

    print("\n=== CNF Parsed Grammar ===")
    for k, v in R.items():
        print(f"{k} → {v}")

    return R


