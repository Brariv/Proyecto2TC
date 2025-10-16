from fa_types.nfa import State as NFAState

class State:
    def __init__(self, closure:set[tuple[NFAState,int]]):
        self.closure = closure 
        self.edges = {} # for referencing another state, we just check is closure, cause we know they won't repeat

