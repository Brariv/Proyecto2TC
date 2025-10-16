def grammar_parsing(grammar_string: str) -> tuple[list[str], list[str], dict[str, list[list[str]]]]:
    grammar_array = grammar_string.splitlines()
    for i in range(len(grammar_array)):
        grammar_array[i] = grammar_array[i].split(" ")
    
    non_terminals = []
    terminals = []
    R = {}

    for i in range(len(grammar_array)):
        if grammar_array[i][0] not in non_terminals:
            non_terminals.append(grammar_array[i][0])
        # if grammar_array[i][2] not in R:
        #     R[grammar_array[i][2]] = []
        
        for j in range(3, len(grammar_array[i])):
            if grammar_array[i][j] not in terminals and grammar_array[i][j] not in non_terminals and grammar_array[i][j] != '|':
                terminals.append(grammar_array[i][j])

        Rule = []
        SubRule = []
        for j in range(2, len(grammar_array[i])):
            if grammar_array[i][j] != '|':
                SubRule.append(grammar_array[i][j])
            if grammar_array[i][j] == '|' or j == len(grammar_array[i]) - 1:
                if len(SubRule) > 0:
                    Rule.append(SubRule)
                    SubRule = []

            print("Rule for", grammar_array[i][0], ":", Rule)
        
        R[grammar_array[i][0]] = Rule
    return non_terminals, terminals, R


