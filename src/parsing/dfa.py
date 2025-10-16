import json
from typing import Any, Optional

from fa_types.nfa import State as NFAState
from fa_types.dfa import State as DFAState


def _jsonToDfa(json_str: str) -> DFAState:

    data = json.loads(json_str)
    states_raw = data["states"]

    id_to_state: dict[int, DFAState] = {}

    # create shells with correctly-typed closures
    for entry in states_raw:
        closure_serialized = entry.get("closure", [])
        closure_set: set[tuple[NFAState, int]] = set()

        for item in closure_serialized:
            if isinstance(item, int):
                # normal case: (NFAState placeholder, idx)
                closure_set.add((NFAState(), item))
            else:
                # fallback for non-int items: create placeholder with label,
                # use -1 as sentinel idx to keep the type int
                closure_set.add((NFAState(label=str(item)), -1))

        id_to_state[entry["id"]] = DFAState(closure_set)

    # wire edges
    for entry in states_raw:
        s = id_to_state[entry["id"]]
        for sym, target in entry.get("edges", {}).items():
            s.edges[str(sym)] = id_to_state[target]

    return id_to_state[data["start"]]

def loadDfaFromFile(path: str) -> DFAState:
    with open(path, "r", encoding="utf-8") as fh:
        js = fh.read()
    return _jsonToDfa(js)
