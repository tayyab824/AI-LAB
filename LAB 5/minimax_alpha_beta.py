"""
Minimax and Alpha-Beta Pruning lab.
A complete binary game tree is defined below because no supplied tree diagram
was attached to the task. Root MAX; next level MIN; next level MAX; leaves numeric.
"""
TREE = {
    "R": ["A", "B"],
    "A": ["A1", "A2"],
    "B": ["B1", "B2"],
    "A1": [3, 5],
    "A2": [6, 9],
    "B1": [1, 2],
    "B2": [0, -1],
}

def minimax(node, maximizing, counter, trace=None):
    """Return minimax value and count each terminal leaf exactly once."""
    if isinstance(node, (int, float)):
        counter[0] += 1
        if trace is not None:
            trace.append(("LEAF", node))
        return node

    values = [minimax(child, not maximizing, counter, trace) for child in TREE[node]]
    value = max(values) if maximizing else min(values)
    if trace is not None:
        trace.append(("NODE", node, "MAX" if maximizing else "MIN", values, value))
    return value

def alpha_beta(node, maximizing, alpha, beta, counter, trace=None):
    """Return minimax value and count evaluated terminal leaves."""
    if isinstance(node, (int, float)):
        counter[0] += 1
        if trace is not None:
            trace.append(("LEAF", node))
        return node

    if maximizing:
        value = float("-inf")
        for child in TREE[node]:
            value = max(value, alpha_beta(child, False, alpha, beta, counter, trace))
            alpha = max(alpha, value)
            if alpha >= beta:
                if trace is not None:
                    trace.append(("PRUNE", node, "remaining children", TREE[node][TREE[node].index(child)+1:]))
                break
        if trace is not None:
            trace.append(("NODE", node, "MAX", value))
        return value
    else:
        value = float("inf")
        for child in TREE[node]:
            value = min(value, alpha_beta(child, True, alpha, beta, counter, trace))
            beta = min(beta, value)
            if alpha >= beta:
                if trace is not None:
                    trace.append(("PRUNE", node, "remaining children", TREE[node][TREE[node].index(child)+1:]))
                break
        if trace is not None:
            trace.append(("NODE", node, "MIN", value))
        return value

def run_order(label):
    m_count=[0]; a_count=[0]
    mt=[]; at=[]
    mv=minimax("R", True, m_count, mt)
    av=alpha_beta("R", True, float("-inf"), float("inf"), a_count, at)
    print(f"\\n--- {label} ---")
    print("Minimax value:",mv,"leaf evaluations:",m_count[0])
    print("Alpha-beta value:",av,"leaf evaluations:",a_count[0])
    print("Alpha-beta trace:")
    for item in at: print(" ",item)
    assert mv == av
    return mv,m_count[0],a_count[0]

if __name__=="__main__":
    print("TREE: R(MAX) -> A,B(MIN) -> A1,A2,B1,B2(MAX) -> leaves")
    print("Original leaf values: A1=[3,5], A2=[6,9], B1=[1,2], B2=[0,-1]")
    original=run_order("Original left-to-right order")
    # Reverse the order of the two children at each internal level.
    TREE["R"]=["B","A"]
    TREE["A"]=["A2","A1"]
    TREE["B"]=["B2","B1"]
    reordered=run_order("Reordered branches")
    print("\\nSUMMARY")
    print("Original: root value =",original[0],", Minimax leaves =",original[1],
          ", Alpha-beta leaves =",original[2])
    print("Reordered: root value =",reordered[0],", Minimax leaves =",reordered[1],
          ", Alpha-beta leaves =",reordered[2])
    print("Root value stays the same; alpha-beta leaf work can change with branch order.")
