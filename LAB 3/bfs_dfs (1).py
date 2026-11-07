"""
Lab 3 - BFS and DFS
Assumed directed search graph (successor order is important):
A: B, C
B: A, D, E
C: A, F
D: B, G
E: B, G
F: C, G
G: D, E, F

Search stops when G is removed from the frontier and processed.
"""
from collections import deque

GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "G"],
    "E": ["B", "G"],
    "F": ["C", "G"],
    "G": ["D", "E", "F"],
}

def bfs(start="A", goal="G"):
    frontier = deque([[start]])
    discovered = {start}
    order = []
    step = 0
    while frontier:
        path = frontier.popleft()
        node = path[-1]
        step += 1
        order.append(node)
        print(f"BFS {step}: process={node}, queue={[p[-1] for p in frontier]}")
        if node == goal:
            print("BFS path:", " -> ".join(path))
            print("BFS visit order:", order)
            return path, order
        for nxt in GRAPH[node]:
            if nxt not in discovered:
                discovered.add(nxt)
                frontier.append(path + [nxt])
        print(f"       after expansion queue={[p[-1] for p in frontier]}")
    return None, order

def dfs(start="A", goal="G"):
    # Stack stores complete paths. Reverse insertion preserves listed successor order.
    stack = [[start]]
    discovered = {start}
    order = []
    step = 0
    while stack:
        path = stack.pop()
        node = path[-1]
        step += 1
        order.append(node)
        print(f"DFS {step}: process={node}, stack(top first)={[p[-1] for p in reversed(stack)]}")
        if node == goal:
            print("DFS path:", " -> ".join(path))
            print("DFS visit order:", order)
            return path, order
        for nxt in reversed(GRAPH[node]):
            if nxt not in discovered:
                discovered.add(nxt)
                stack.append(path + [nxt])
        print(f"       after expansion stack(top first)={[p[-1] for p in reversed(stack)]}")
    return None, order

if __name__ == "__main__":
    bfs()
    print()
    dfs()
