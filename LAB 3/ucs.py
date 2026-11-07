"""
Lab 3 - Uniform Cost Search.
Weighted extension of the same graph. An added direct corridor A-G is included.
All edges are undirected and the same weight applies in both directions.
"""
import heapq

WEIGHTED_GRAPH = {
    "A": [("B", 1), ("C", 2), ("G", 10)],  # A-G is the added corridor
    "B": [("A", 1), ("D", 1), ("E", 4)],
    "C": [("A", 2), ("F", 2)],
    "D": [("B", 1), ("G", 1)],
    "E": [("B", 4), ("G", 1)],
    "F": [("C", 2), ("G", 2)],
    "G": [("D", 1), ("E", 1), ("F", 2), ("A", 10)],
}

def ucs(start="A", goal="G"):
    frontier = [(0, start, [start])]
    best_cost = {start: 0}
    processed = []
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if cost != best_cost.get(node):
            continue
        processed.append((node, cost))
        print(f"Process {node} at cumulative cost {cost}")
        if node == goal:
            print("UCS path:", " -> ".join(path))
            print("UCS cost:", cost)
            print("Processing order:", [n for n, _ in processed])
            return path, cost, processed
        for nxt, weight in WEIGHTED_GRAPH[node]:
            new_cost = cost + weight
            if new_cost < best_cost.get(nxt, float("inf")):
                best_cost[nxt] = new_cost
                heapq.heappush(frontier, (new_cost, nxt, path + [nxt]))
    return None, float("inf"), processed

def path_cost(path):
    total = 0
    for a, b in zip(path, path[1:]):
        total += next(w for n, w in WEIGHTED_GRAPH[a] if n == b)
    return total

if __name__ == "__main__":
    path, cost, _ = ucs()
    print("Independent path-cost check:", path_cost(path))
    print("BFS route on same topology: A -> G, cost =", path_cost(["A", "G"]))
