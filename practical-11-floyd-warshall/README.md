# Practical 11: Floyd-Warshall Algorithm (All Pairs Shortest Paths)

This practical demonstrates the **Floyd-Warshall Algorithm**, a **Dynamic Programming** algorithm that finds the **shortest paths between every pair of vertices** in a weighted graph. The graph is **predefined** inside the program, so **no user input is required**.

---

## Problem Statement

Given a weighted directed graph represented as an adjacency matrix, find the **shortest path distance between every pair of vertices**. If no path exists between two vertices, the distance remains `INF` (infinity).

---

## Key Idea

The Floyd-Warshall algorithm considers every vertex `k` as a possible **intermediate vertex** for every pair `(i, j)`:

```
dist[i][j] = min( dist[i][j], dist[i][k] + dist[k][j] )
```

After considering all vertices as intermediates, `dist[i][j]` holds the shortest distance from vertex `i` to vertex `j`. This works because the sub-problems build up gradually — after iteration `k`, `dist[i][j]` uses only intermediate vertices from `{0, 1, ..., k}`.

### Predefined Graph (adjacency matrix, `INF` = no direct edge)

```
      A    B    C    D
A    0    3    8   inf
B  inf    0   inf   1
C  inf    4    0   inf
D    2   inf  inf   0
```

---

## Time and Space Complexity

| Algorithm | Time Complexity | Space Complexity |
| :--- | :---: | :---: |
| Floyd-Warshall | $O(V^3)$ | $O(V^2)$ |

The triple nested loop over all `V` vertices gives the cubic time complexity. The `V x V` distance matrix gives quadratic space.

---

## Python Program

```python
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
```

---

## Example Output

```text
Floyd-Warshall Algorithm - All Pairs Shortest Paths
----------------------------------------------------
Graph is predefined (weighted directed graph), NO user input required.

Input Graph (adjacency matrix, INF = no direct edge):
         A     B     C     D
 A       0     3     8   inf
 B     inf     0   inf     1
 C     inf     4     0   inf
 D       2   inf   inf     0

All-Pairs Shortest Path Distance Matrix:
         A     B     C     D
 A       0     3     8     4
 B       3     0    11     1
 C       7     4     0     5
 D       2     5    10     0

--- Time Complexity ---
Floyd-Warshall Algorithm: O(V^3)

--- Space Complexity ---
O(V^2) for the distance matrix

Execution Time: 0.000024800 seconds
```

For example, the shortest path from `A` to `D` is `A -> B -> D` with total distance `3 + 1 = 4`, which is better than going directly (`INF` = no direct edge).

---

## How to Run

```bash
cd practical-11-floyd-warshall
python floyd_warshall.py
```

---

## Author

**Gnaneswar Vuyyuri**
