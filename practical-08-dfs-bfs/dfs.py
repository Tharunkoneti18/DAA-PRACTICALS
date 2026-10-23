import time

# Predefined graph (adjacency list) - NO user input required
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


def dfs_traversal(graph, start):
    """Returns the Depth First Search traversal order using an explicit stack."""
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Push neighbors in reverse so we visit them in the same order
            # as they appear in the adjacency list.
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


def main():
    start_node = 'A'
    print("Depth First Search (DFS) Traversal on a Predefined Graph")
    print("---------------------------------------------------------")
    print(f"Graph (adjacency list): {graph}")
    print(f"Start node: {start_node}\n")

    start_time = time.perf_counter()
    dfs_order = dfs_traversal(graph, start_node)
    end_time = time.perf_counter()

    print("DFS Traversal:", " -> ".join(dfs_order))

    print("\n--- Time Complexity ---")
    print("DFS: O(V + E)  (V = number of vertices, E = number of edges)")

    print("\n--- Space Complexity ---")
    print("DFS: O(V) worst case (visited set + stack)")

    print(f"\nExecution Time: {end_time - start_time:.9f} seconds")


if __name__ == "__main__":
    main()