# Write a program in Python to implement Dijkstra’s algorithm to find the shortest path from a source vertex.

import heapq

def dijkstra(graph, source):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Priority queue (min-heap)
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Update shortest distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage
graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 1)],
    'C': [('B', 2), ('D', 5)],
    'D': []
}

source = 'A'
shortest_paths = dijkstra(graph, source)

print("Shortest distances from source:", source)
for node in shortest_paths:
    print(f"{node} -> {shortest_paths[node]}")