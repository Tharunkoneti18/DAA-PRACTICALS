# Practical 9: Prim's Algorithm (Minimum Cost Spanning Tree)

This practical demonstrates **Prim's Algorithm**, a greedy algorithm that computes the **Minimum Cost Spanning Tree (MST)** of a weighted, undirected graph. The graph is **predefined** inside the program, so **no user input is required**.

---

## Problem Statement

Given a connected, weighted undirected graph, find the **Minimum Spanning Tree (MST)** — the subset of edges that connects all the vertices together without any cycles and with the **minimum possible total edge weight**. The program prints every edge selected in the MST with its weight, the total MST cost, and the execution time.

---

## Key Idea

Prim's algorithm grows the MST **one vertex at a time**, starting from an arbitrary vertex:

1. Maintain a set of vertices already included in the MST.
2. Keep an array `min_edge[v]` = the cheapest edge weight that connects vertex `v` to the tree so far.
3. Repeatedly pick the **unvisited** vertex with the smallest `min_edge` value, add it to the tree, and update `min_edge` for all of its neighbours.

The greedy choice — always adding the cheapest edge that connects a new vertex to the growing tree — guarantees a minimum spanning tree overall.

### Predefined Graph (adjacency matrix, `INF` = no direct edge)

```
      A    B    C    D    E    F
A    0    6    1    5   inf  inf
B    6    0    5   inf   3   inf
C    1    5    0    5    6    4
D    5   inf   5    0   inf   2
E   inf   3    6   inf   0    6
F   inf  inf   4    2    6    0
```

---

## Time and Space Complexity

| Algorithm | Time Complexity | Space Complexity |
| :--- | :---: | :---: |
| Prim's Algorithm (adjacency matrix based) | $O(V^2)$ | $O(V)$ |

The outer loop runs $V$ times, and finding the minimum edge plus the update step each scan $V$ vertices, giving $O(V^2)$ time. Only three arrays of size $V$ (`min_edge`, `visited`, `parent`) are used, so space is $O(V)$.

---

## Python Program

```python
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
```

---

## Example Output

```text
Prim's Algorithm - Minimum Cost Spanning Tree
----------------------------------------------
Graph is predefined (weighted undirected graph), NO user input required.

Weighted Graph (adjacency matrix, INF = no direct edge):
         A     B     C     D     E     F
 A     inf     6     1     5   inf   inf
 B       6   inf     5   inf     3   inf
 C       1     5   inf     5     6     4
 D       5   inf     5   inf   inf     2
 E     inf     3     6   inf   inf     6
 F     inf   inf     4     2     6   inf

--- Minimum Spanning Tree (MST) ---
A -- C   weight = 1
C -- F   weight = 4
F -- D   weight = 2
C -- B   weight = 5
B -- E   weight = 3

Total MST Cost: 15

--- Time Complexity ---
Prim's Algorithm (adjacency matrix): O(V^2)

--- Space Complexity ---
O(V) for the min_edge, visited and parent arrays

Execution Time: 0.000019700 seconds
```

---

## How to Run

```bash
cd practical-09-prims-algorithm
python prims_algorithm.py
```

---

## Author

**Gnaneswar Vuyyuri**
