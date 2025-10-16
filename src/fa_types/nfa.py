from typing import Optional


class State:
    def __init__(self, label: Optional[str] = None):
        self.label = label # instead of having explictly put the label in each edge, it's more intuitive to look at the labels as the one which contains the character (but you could put the label in the edge)
        # as we know, the Thompson algorithm will construct the ThompsonsNFA with only to possible edges per state
        self.edge1:Optional[State] = None # to what Other state is referencing
        self.edge2:Optional[State] = None# to what Other state is referencing

