"""
Lab 3 - Depth-Limited Search and Iterative Deepening DFS.
The root is at depth 0. The graph and successor order match lab3_bfs_dfs.py.
"""
GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "G"],
    "E": ["B", "G"],
    "F": ["C", "G"],
    "G": ["D", "E", "F"],
}

FOUND, CUTOFF, FAILURE = "FOUND", "CUTOFF", "FAILURE"

def dls(start, goal, limit):
    """Return (status, path). Cycle check is local to the current path."""
    def visit(node, path, depth):
        if node == goal:
            return FOUND, path
        cutoff_occurred = False

        if depth == limit:
            # If there is any successor not already on this path, more depth
            # could be useful, so the search is cut off at this boundary.
            if any(n not in path for n in GRAPH[node]):
                return CUTOFF, None
            return FAILURE, None

        for nxt in GRAPH[node]:
            if nxt in path:
                continue
            status, result = visit(nxt, path + [nxt], depth + 1)
            if status == FOUND:
                return FOUND, result
            if status == CUTOFF:
                cutoff_occurred = True

        return (CUTOFF, None) if cutoff_occurred else (FAILURE, None)

    return visit(start, [start], 0)

def iddfs(start, goal, max_depth):
    attempts = []
    for limit in range(1, max_depth + 1):
        status, path = dls(start, goal, limit)
        attempts.append((limit, status, path))
        if status == FOUND:
            return status, path, attempts
        if status == FAILURE:
            return status, None, attempts
    return CUTOFF, None, attempts

if __name__ == "__main__":
    for limit in range(1, 5):
        status, path = dls("A", "G", limit)
        print(f"DLS limit={limit}: {status}; path={path}")

    print("\nIDDFS:")
    for maximum in range(1, 5):
        status, path, attempts = iddfs("A", "G", maximum)
        attempted = [x[0] for x in attempts]
        print(f"max_depth={maximum}: {status}; attempts={attempted}; path={path}")
