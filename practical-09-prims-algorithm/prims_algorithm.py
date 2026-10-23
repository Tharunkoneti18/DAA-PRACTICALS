import time

# Predefined weighted undirected graph (adjacency matrix) - NO user input required.
# Vertices: 0='A', 1='B', 2='C', 3='D', 4='E', 5='F'
INF = float('inf')  # INF means there is no direct edge between the two vertices

graph = [
    [INF, 6, 1, 5, INF, INF],
    [6, INF, 5, INF, 3, INF],
    [1, 5, INF, 5, 6, 4],
    [5, INF, 5, INF, INF, 2],
    [INF, 3, 6, INF, INF, 6],
    [INF, INF, 4, 2, 6, INF],
]

vertices = ['A', 'B', 'C', 'D', 'E', 'F']


def prims_mst(graph, start=0):
    """Returns the Minimum Spanning Tree (MST) edges and total cost using Prim's algorithm."""
    n = len(graph)

    visited = [False] * n   # set of vertices already included in the MST
    min_edge = [INF] * n    # cheapest edge weight connecting each vertex to the tree
    parent = [-1] * n       # parent of each vertex inside the MST

    min_edge[start] = 0
    mst_edges = []
    total_cost = 0

    for _ in range(n):
        # Pick the unvisited vertex with the smallest min_edge value
        u = -1
        best = INF
        for v in range(n):
            if not visited[v] and min_edge[v] < best:
                best = min_edge[v]
                u = v

        if u == -1:   # no reachable vertex -> graph is disconnected
            break

        visited[u] = True
        total_cost += min_edge[u]

        if parent[u] != -1:
            mst_edges.append((parent[u], u, min_edge[u]))

        # Update min_edge for all neighbours of u
        for v in range(n):
            if not visited[v] and graph[u][v] < min_edge[v]:
                min_edge[v] = graph[u][v]
                parent[v] = u

    return total_cost, mst_edges


def print_matrix(matrix, header):
    """Prints the adjacency matrix in a readable format."""
    print(header)
    print("    " + "".join(f"{v:>6}" for v in vertices))
    for i, row in enumerate(matrix):
        values = "".join(f"{'inf' if val == INF else val:>6}" for val in row)
        print(f" {vertices[i]}  {values}")


def main():
    print("Prim's Algorithm - Minimum Cost Spanning Tree")
    print("----------------------------------------------")
    print("Graph is predefined (weighted undirected graph), NO user input required.\n")

    print_matrix(graph, "Weighted Graph (adjacency matrix, INF = no direct edge):")

    start_time = time.perf_counter()
    total_cost, mst_edges = prims_mst(graph)
    end_time = time.perf_counter()

    print("\n--- Minimum Spanning Tree (MST) ---")
    for u, v, w in mst_edges:
        print(f"{vertices[u]} -- {vertices[v]}   weight = {w}")
    print(f"\nTotal MST Cost: {total_cost}")

    print("\n--- Time Complexity ---")
    print("Prim's Algorithm (adjacency matrix): O(V^2)")

    print("\n--- Space Complexity ---")
    print("O(V) for the min_edge, visited and parent arrays")

    print(f"\nExecution Time: {end_time - start_time:.9f} seconds")


if __name__ == "__main__":
    main()
