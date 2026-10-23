import time

# Predefined weighted directed graph (adjacency matrix) - NO user input required.
# Vertices: 0='A', 1='B', 2='C', 3='D'. INF means no direct edge.
INF = float('inf')

graph = [
    [0, 3, 8, INF],
    [INF, 0, INF, 1],
    [INF, 4, 0, INF],
    [2, INF, INF, 0],
]

vertices = ['A', 'B', 'C', 'D']


def floyd_warshall(graph):
    """Returns the all-pairs shortest path distance matrix using the Floyd-Warshall algorithm."""
    n = len(graph)
    dist = [row[:] for row in graph]   # working copy of the distance matrix

    # Consider every vertex as an intermediate vertex
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_matrix(matrix, header):
    """Prints a matrix in a readable format."""
    print(header)
    print("    " + "".join(f"{v:>6}" for v in vertices))
    for i, row in enumerate(matrix):
        values = "".join(f"{'inf' if val == INF else val:>6}" for val in row)
        print(f" {vertices[i]}  {values}")


def main():
    print("Floyd-Warshall Algorithm - All Pairs Shortest Paths")
    print("----------------------------------------------------")
    print("Graph is predefined (weighted directed graph), NO user input required.\n")

    print_matrix(graph, "Input Graph (adjacency matrix, INF = no direct edge):")

    start_time = time.perf_counter()
    dist = floyd_warshall(graph)
    end_time = time.perf_counter()

    print()
    print_matrix(dist, "All-Pairs Shortest Path Distance Matrix:")

    print("\n--- Time Complexity ---")
    print("Floyd-Warshall Algorithm: O(V^3)")

    print("\n--- Space Complexity ---")
    print("O(V^2) for the distance matrix")

    print(f"\nExecution Time: {end_time - start_time:.9f} seconds")


if __name__ == "__main__":
    main()
