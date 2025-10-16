def grammar_parsing(Grammar_String: str) -> tuple[list[str], list[str], dict[str, list[list[str]]]]:
    Grammar_Array = Grammar_String.splitlines()
    for i in range(len(Grammar_Array)):
        Grammar_Array[i] = Grammar_Array[i].split(" ")
    
    non_terminals = []
    terminals = []
    R = {}

    for i in range(len(Grammar_Array)):
        if Grammar_Array[i][0] not in non_terminals:
            non_terminals.append(Grammar_Array[i][0])
        # if Grammar_Array[i][2] not in R:
        #     R[Grammar_Array[i][2]] = []
        
        for j in range(3, len(Grammar_Array[i])):
            if Grammar_Array[i][j] not in terminals and Grammar_Array[i][j] not in non_terminals and Grammar_Array[i][j] != '|':
                terminals.append(Grammar_Array[i][j])

        Rule = []
        SubRule = []
        for j in range(2, len(Grammar_Array[i])):
            if Grammar_Array[i][j] != '|':
                SubRule.append(Grammar_Array[i][j])
            if Grammar_Array[i][j] == '|' or j == len(Grammar_Array[i]) - 1:
                if len(SubRule) > 0:
                    Rule.append(SubRule)
                    SubRule = []

            print("Rule for", Grammar_Array[i][0], ":", Rule)
        
        R[Grammar_Array[i][0]] = Rule
    return non_terminals, terminals, R


# non_terminals, terminals, R = Grammar_PreParser(Grammar_Array)
# print("Non Terminals: ", non_terminals)
# print(" ")
# print("Terminals: ", terminals)
# print(" ")
# print("R: ", R)