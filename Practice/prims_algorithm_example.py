# Write a program in Python to implement Prim’s Algorithm for finding theMinimum Cost Spanning Tree.


import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, vertex)
    mst = []
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        # Skip if already visited
        if u in visited:
            continue

        visited.add(u)
        total_cost += weight

        if weight != 0:
            mst.append((u, weight))

        # Add neighbors to heap
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))

    return mst, total_cost


# Example usage
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

mst, cost = prim(graph, 'A')

print("Minimum Spanning Tree:")
for node, weight in mst:
    print(f"{node} with edge weight {weight}")

print("Total Cost:", cost)