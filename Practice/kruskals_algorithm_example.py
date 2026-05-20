# Write a program in Python to implement Kruskal’s algorithm to find the Minimum Cost Spanning Tree of a graph.


# Disjoint Set (Union-Find)
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


# Kruskal's Algorithm
def kruskal(vertices, edges):
    # Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])

    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        # Check if adding edge forms a cycle
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


# Example usage
vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 6),
    ('C', 'D', 4)
]

mst, cost = kruskal(vertices, edges)

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")

print("Total Cost:", cost)