# Function to perform the CYK Algorithm
def cyk_parsing(word: str, R: dict[str, list[list[str]]]) -> bool:
    n = len(word)

    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]

    # Filling in the table
    for j in range(0, n):

        # Iterate over the rules
        for lhs, rule in R.items():
            for rhs in rule:
                
                # If a terminal is found
                if len(rhs) == 1 and \
                rhs[0] == word[j]:
                    T[j][j].add(lhs)

        for i in range(j, -1, -1):   
            
            # Iterate over the range i to j + 1   
            for k in range(i, j + 1):     

                # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:
                        
                        # If a terminal is found
                        if len(rhs) == 2 and \
                        k + 1 <= j and \
                        rhs[0] in T[i][k] and \
                        rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)

    # If word can be formed by rules 
    # of given grammar
    if len(T[0][n-1]) != 0:
        return True
    else:
        return False