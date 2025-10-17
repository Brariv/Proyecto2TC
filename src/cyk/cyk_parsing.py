# Function to perform the CYK Algorithm
def cyk_parsing(word: list[str], R: dict[str, list[list[str]]]) -> bool:
    n = len(word) # n is its length — this determines the size of the parsing table.

    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]
    # Example for w = "abc" (n=3):
    #       j=0   j=1   j=2
    # i=0 [ {}  | {}  | {} ]
    # i=1 [     | {}  | {} ]
    # i=2 [     |     | {} ]

    # Filling in the table
    # Fill the diagonal — base case (single characters or words)
    for j in range(0, n):

        # Iterate over the rules
        for lhs, rule in R.items(): # lhs is the left-hand side, rule is the list of productions
            for rhs in rule:
                
                # If a terminal is found
                if len(rhs) == 1 and \
                rhs[0] == word[j]: # if the rule matches the character at position j
                    T[j][j].add(lhs) # If a production A → a matches the terminal w[j], then record that A can produce that single letter.
            
            # If w = "ab", and grammar has A → a and B → b,
            # T[0][0] = {A}
            # T[1][1] = {B}

        for i in range(j, -1, -1): # For every substring w[i..j],
            
            # Iterate over the range i to j + 1   
            for k in range(i, j + 1):  # try splitting it at every possible midpoint k,

                # Iterate over the rules
                for lhs, rule in R.items():
                    
                    for rhs in rule:
                        
                        # If a terminal is found
                        # and see if there’s a rule A → BC where:
                        # B can produce the left substring w[i..k]
                        # C can produce the right substring w[k+1..j]
                        
                        
                        if len(rhs) == 2 and \
                           k + 1 <= j and \
                           rhs[0] in T[i][k] and \
                           rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)
                        elif len(rhs) == 1:
                            # handle unit productions A -> B (or redundant terminal check)
                            # if the single symbol can produce w[i..j], add lhs
                            if rhs[0] in T[i][j] or (i == j and rhs[0] == word[j]):
                                T[i][j].add(lhs)

    # If word can be formed by rules 
    # of given grammar
    # The top of the triangle T[0][n-1] corresponds to the whole input string.
    # If it contains the start symbol (like S), the string belongs to the grammar.
    
    if len(T[0][n-1]) != 0:
        return True
    else:
        return False
    
    # === Grammar Example ===
    # S → AB | BC
    # A → BA | a
    # B → CC | b
    # C → AB | a

    # String: "ba"

    # Substring     Nonterminals
    #   "b"          {B}
    #   "a"          {A, C}
    #   "ba"         {S, A, C}

    # S ∈ T[0][1]a string accepted.
