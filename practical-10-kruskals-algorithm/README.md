# Practical 10: Kruskal's Algorithm (Minimum Cost Spanning Tree)

This practical demonstrates **Kruskal's Algorithm**, a greedy algorithm that computes the **Minimum Cost Spanning Tree (MST)** of a weighted, undirected graph using a **Union-Find (Disjoint Set)** data structure. The graph is **predefined** inside the program, so **no user input is required**.

---

## Problem Statement

Given a connected, weighted undirected graph, find the **Minimum Spanning Tree (MST)** — the subset of edges that connects all the vertices together without any cycles and with the **minimum possible total edge weight**. The program prints every edge selected in the MST with its weight, the total MST cost, and the execution time.

---

## Key Idea

Kruskal's algorithm builds the MST by processing edges in **increasing order of weight**:

1. Sort all edges by weight (ascending).
2. Pick the cheapest edge. If adding it **does not create a cycle** (its two end vertices belong to different sets), add it to the MST.
3. Repeat until `V - 1` edges have been added.

Cycle detection is done with a **Union-Find (Disjoint Set)** data structure supporting:
- `find(x)` → returns the root of the set containing `x` (**path compression** for speed).
- `union(x, y)` → merges the sets of `x` and `y` (**union by rank**); returns `False` if they were already in the same set (cycle).

### Predefined Graph (edge list, `(u, v, weight)`)

```
A -- B : 6       B -- E : 3       D -- F : 2
A -- C : 1       C -- B : 5       C -- D : 5
A -- D : 5       C -- E : 6       B -- C : 5
C -- F : 4       E -- F : 6
```

---

## Time and Space Complexity

| Algorithm | Time Complexity | Space Complexity |
| :--- | :---: | :---: |
| Kruskal's Algorithm | $O(E \log E)$ | $O(V + E)$ |

Sorting all `E` edges dominates the cost, hence $O(E \log E)$. The disjoint set and the edge list use $O(V + E)$ space.

---

## Python Program

```python
import time

# Predefined weighted undirected graph (edge list) - NO user input required.
# Each edge is a tuple (u, v, weight).
# Vertices: 0='A', 1='B', 2='C', 3='D', 4='E', 5='F'
edges = [
    (0, 1, 6),
    (0, 2, 1),
    (0, 3, 5),
    (1, 2, 5),
    (1, 4, 3),
    (2, 3, 5),
    (2, 4, 6),
    (2, 5, 4),
    (3, 5, 2),
    (4, 5, 6),
]

num_vertices = 6
vertices = ['A', 'B', 'C', 'D', 'E', 'F']


class DisjointSet:
    """Union-Find (disjoint set) data structure used for cycle detection."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Returns the representative (root) of the set containing x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Merges the sets of x and y. Returns True if merged, False if they form a cycle."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # same set -> adding this edge would create a cycle

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskals_mst(num_vertices, edges):
    """Returns the Minimum Spanning Tree (MST) edges and total cost using Kruskal's algorithm."""
    dsu = DisjointSet(num_vertices)
    mst_edges = []
    total_cost = 0

    # Sort all edges by weight in ascending order
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    for u, v, w in sorted_edges:
        if dsu.union(u, v):        # edge does not form a cycle
            mst_edges.append((u, v, w))
            total_cost += w
            if len(mst_edges) == num_vertices - 1:
                break               # MST is complete

    return total_cost, mst_edges


def main():
    print("Kruskal's Algorithm - Minimum Cost Spanning Tree")
    print("------------------------------------------------")
    print("Graph is predefined (weighted undirected graph), NO user input required.\n")

    print("Weighted Graph (edge list, sorted by weight):")
    for u, v, w in sorted(edges, key=lambda edge: edge[2]):
        print(f"  {vertices[u]} -- {vertices[v]}   weight = {w}")

    start_time = time.perf_counter()
    total_cost, mst_edges = kruskals_mst(num_vertices, edges)
    end_time = time.perf_counter()

    print("\n--- Minimum Spanning Tree (MST) ---")
    for u, v, w in mst_edges:
        print(f"{vertices[u]} -- {vertices[v]}   weight = {w}")
    print(f"\nTotal MST Cost: {total_cost}")

    print("\n--- Time Complexity ---")
    print("Kruskal's Algorithm: O(E log E)   (E = number of edges)")

    print("\n--- Space Complexity ---")
    print("O(V + E) for the disjoint set and the edge list")

    print(f"\nExecution Time: {end_time - start_time:.9f} seconds")


if __name__ == "__main__":
    main()
```

---

## Example Output

```text
Kruskal's Algorithm - Minimum Cost Spanning Tree
------------------------------------------------
Graph is predefined (weighted undirected graph), NO user input required.

Weighted Graph (edge list, sorted by weight):
  A -- C   weight = 1
  D -- F   weight = 2
  B -- E   weight = 3
  C -- F   weight = 4
  A -- D   weight = 5
  B -- C   weight = 5
  C -- D   weight = 5
  A -- B   weight = 6
  C -- E   weight = 6
  E -- F   weight = 6

--- Minimum Spanning Tree (MST) ---
A -- C   weight = 1
D -- F   weight = 2
B -- E   weight = 3
C -- F   weight = 4
B -- C   weight = 5

Total MST Cost: 15

--- Time Complexity ---
Kruskal's Algorithm: O(E log E)   (E = number of edges)

--- Space Complexity ---
O(V + E) for the disjoint set and the edge list

Execution Time: 0.000092900 seconds
```

> **Note:** This MST (total cost 15) is the same tree produced by **Prim's Algorithm in Practical 9** — both algorithms always return a minimum spanning tree of the same weight.

---

## How to Run

```bash
cd practical-10-kruskals-algorithm
python kruskals_algorithm.py
```

---

## Author

**Gnaneswar Vuyyuri**

