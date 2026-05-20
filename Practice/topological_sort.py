# Write a program in Python to implement Topological Sort for a directed acyclic graph (DAG).

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edge
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Recursive helper function
    def topological_sort_util(self, v, visited, stack):
        visited.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.topological_sort_util(neighbor, visited, stack)

        # Push current node to stack after visiting neighbors
        stack.append(v)

    # Topological Sort function
    def topological_sort(self):
        visited = set()
        stack = []

        for vertex in list(self.graph):
            if vertex not in visited:
                self.topological_sort_util(vertex, visited, stack)

        # Return reversed stack
        return stack[::-1]


# Example usage
g = Graph()
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')

result = g.topological_sort()

print("Topological Sort:")
print(result)
