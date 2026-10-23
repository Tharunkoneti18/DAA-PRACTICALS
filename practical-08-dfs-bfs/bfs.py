import time
from collections import deque

# Predefined graph (adjacency list) - NO user input required
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


def bfs_traversal(graph, start):
    """Returns the Breadth First Search traversal order using a queue."""
    visited = set()
    queue = deque([start])
    order = []

    visited.add(start)
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def main():
    start_node = 'A'
    print("Breadth First Search (BFS) Traversal on a Predefined Graph")
    print("-----------------------------------------------------------")
    print(f"Graph (adjacency list): {graph}")
    print(f"Start node: {start_node}\n")

    start_time = time.perf_counter()
    bfs_order = bfs_traversal(graph, start_node)
    end_time = time.perf_counter()

    print("BFS Traversal:", " -> ".join(bfs_order))

    print("\n--- Time Complexity ---")
    print("BFS: O(V + E)  (V = number of vertices, E = number of edges)")

    print("\n--- Space Complexity ---")
    print("BFS: O(V) worst case (visited set + queue)")

    print(f"\nExecution Time: {end_time - start_time:.9f} seconds")


if __name__ == "__main__":
    main()