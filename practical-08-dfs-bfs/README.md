# Practical 8: Depth First Search (DFS) and Breadth First Search (BFS) Traversals

This practical demonstrates **graph traversal** using **Depth First Search (DFS)** and **Breadth First Search (BFS)** in **two separate programs** inside this folder. The graph is **predefined** in each program, so **no user input is required**.

---

## Problem Statement

Given a connected, undirected graph represented as an adjacency list, traverse all its vertices starting from a given node using DFS and BFS and print the order in which the nodes are visited.

This solution uses an **explicit stack** for DFS and a **queue** for BFS, each in its own file.

---

## Files in this Practical

```text
practical-08-dfs-bfs/
├── dfs.py        # Depth First Search traversal only
├── bfs.py        # Breadth First Search traversal only
└── README.md     # Detailed documentation for Practical 08
```

---

## Key Idea

- **DFS (Depth First Search)** explores as far as possible along each branch before backtracking. It is implemented iteratively using a **stack** (LIFO) in `dfs.py`.
- **BFS (Breadth First Search)** explores all neighbours of a node before moving to the next level. It is implemented iteratively using a **queue** (FIFO from `collections.deque`) in `bfs.py`.

Both algorithms use a `visited` set to avoid revisiting nodes and prevent infinite loops (important for graphs with cycles).

Predefined graph used (identical in both programs):

```
A -- B -- D
|    |
E -- C -- F
```

---

## Time and Space Complexity

| Algorithm | File | Time Complexity | Space Complexity |
| :--- | :--- | :---: | :---: |
| DFS | `dfs.py` | $O(V + E)$ | $O(V)$ worst case |
---

## Python Program — DFS (`dfs.py`)

```python
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
```
| BFS | `bfs.py` | $O(V + E)$ | $O(V)$ worst case |

Where $V$ = number of vertices and $E$ = number of edges. Each vertex and edge is visited exactly once, hence the $O(V + E)$ time complexity.
---

## Python Program — BFS (`bfs.py`)

```python
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
```
---

## Example Output

### `dfs.py`
```text
Depth First Search (DFS) Traversal on a Predefined Graph
---------------------------------------------------------
Graph (adjacency list): {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
Start node: A

DFS Traversal: A -> B -> D -> E -> F -> C

--- Time Complexity ---
DFS: O(V + E)

--- Space Complexity ---
DFS: O(V) worst case

Execution Time: 0.000012500 seconds
```

### `bfs.py`
```text
Breadth First Search (BFS) Traversal on a Predefined Graph
-----------------------------------------------------------
Graph (adjacency list): {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
Start node: A

BFS Traversal: A -> B -> C -> D -> E -> F

--- Time Complexity ---
BFS: O(V + E)

--- Space Complexity ---
BFS: O(V) worst case

Execution Time: 0.000009200 seconds
```

---

## How to Run

```bash
cd practical-08-dfs-bfs
python dfs.py   # Depth First Search
python bfs.py   # Breadth First Search
```

---

## Author

**Gnaneswar Vuyyuri**