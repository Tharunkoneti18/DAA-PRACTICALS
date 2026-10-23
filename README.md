# 🧮 Design and Analysis of Algorithms (DAA) Practicals

This repository contains clean, optimized Python implementations of core **Design and Analysis of Algorithms (DAA)** practicals, including step-by-step sorting and searching algorithms, theoretical complexity analyses, and empirical execution time measurements.

---

## 📁 Repository Structure

```text
DAA-practicals/
├── practical-01-sorting-algorithms/
│   ├── bubblesort.py        # Bubble Sort (Optimized with early exit)
│   ├── insertionsort.py     # Insertion Sort
│   ├── mergesort.py         # Merge Sort (Divide & Conquer)
│   ├── quicksort.py         # Quick Sort (Divide & Conquer)
│   ├── selectionsort.py     # Selection Sort
│   └── README.md            # Detailed documentation for Practical 01
├── practical-02-searching-algorithms/
│   ├── linear_search.py     # Linear Search
│   ├── binary_search.py     # Binary Search (Iterative/Recursive)
│   └── README.md            # Detailed documentation for Practical 02
├── practical-03-max-heap/
│   ├── max_heap.py          # Max Heap Operations (Build Heap, Insert, Delete Max)
│   └── README.md            # Detailed documentation for Practical 03
├── practical-04-factorial-comparison/
│   ├── factorial_comparison.py  # Iterative vs Recursive Factorial with timing
│   └── README.md            # Detailed documentation for Practical 04
├── practical-05-knapsack-dp/
│   ├── knapsack_dp.py    # 0/1 Knapsack Problem using Dynamic Programming
│   └── README.md         # Detailed documentation for Practical 05
├── practical-06-matrix-chain-multiplication/
│   ├── matrix_chain_multiplication.py  # Matrix Chain Multiplication using DP
│   └── README.md                     # Detailed documentation for Practical 06
├── practical-07-coin-change-dp/
│   ├── coin_change_dp.py    # Coin Change Problem using Dynamic Programming
│   └── README.md            # Detailed documentation for Practical 07
├── practical-08-dfs-bfs/
│   ├── dfs.py                # Depth First Search traversal (predefined graph, no input)
│   ├── bfs.py                # Breadth First Search traversal (predefined graph, no input)
│   └── README.md             # Detailed documentation for Practical 08
├── practical-09-prims-algorithm/
│   ├── prims_algorithm.py    # Prim's Algorithm (Minimum Spanning Tree, greedy)
│   └── README.md             # Detailed documentation for Practical 09
├── practical-10-kruskals-algorithm/
│   ├── kruskals_algorithm.py # Kruskal's Algorithm (MST using Union-Find)
│   └── README.md             # Detailed documentation for Practical 10
├── practical-11-floyd-warshall/
│   ├── floyd_warshall.py     # Floyd-Warshall (All Pairs Shortest Paths, DP)
│   └── README.md             # Detailed documentation for Practical 11
├── practical-12-travelling-salesman/
│   ├── travelling_salesman.py # Travelling Salesman Problem (Held-Karp DP)
│   └── README.md             # Detailed documentation for Practical 12
├── README.md
```

---

## ⚡ Algorithms & Complexity Summary

### 1. Sorting Algorithms (`practical-01-sorting-algorithms`)

| Algorithm | Best Case Time | Average Case Time | Worst Case Time | Space Complexity | Stability | Strategy |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Bubble Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Stable | Brute Force / Exchange |
| **Selection Sort** | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Unstable | In-Place Selection |
| **Insertion Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Stable | Incremental Insertion |
| **Merge Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ | Stable | Divide and Conquer |
| **Quick Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(\log n)$ | Unstable | Divide and Conquer |

### 2. Searching Algorithms (`practical-02-searching-algorithms`)

| Algorithm | Best Case Time | Average Case Time | Worst Case Time | Space Complexity | Prerequisite |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Linear Search** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Unsorted / Any array |
| **Binary Search** | $\mathcal{O}(1)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | Sorted array required |

### 3. Max Heap (`practical-03-max-heap`)

| Operation | Time Complexity | Auxiliary Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Heapify** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Maintains max heap property downward |
| **Build Max Heap** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Builds max heap from unsorted array |
| **Insertion** | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | Inserts element and sifts upward |
| **Delete Max** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Extracts root and heapifies downward |
### 4. Factorial Calculation — Iterative vs Recursive (`practical-04-factorial-comparison`)

| Method | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Iterative Factorial** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Uses a loop, no extra stack memory |
| **Recursive Factorial** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Uses the function call stack |
### 5. 0/1 Knapsack Problem — Dynamic Programming (`practical-05-knapsack-dp`)

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Dynamic Programming** | $\mathcal{O}(n \times \text{capacity})$ | $\mathcal{O}(n \times \text{capacity})$ | Maximizes value of items within knapsack capacity |

### 6. Matrix Chain Multiplication — Dynamic Programming (`practical-06-matrix-chain-multiplication`)

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Dynamic Programming** | $\mathcal{O}(n^3)$ | $\mathcal{O}(n^2)$ | Finds optimal parenthesization to minimize multiplications |

### 7. Coin Change Problem — Dynamic Programming (`practical-07-coin-change-dp`)

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Dynamic Programming** | $\mathcal{O}(\text{amount} \times \text{coins})$ | $\mathcal{O}(\text{amount})$ | Finds minimum coins for amount via DP table |

### 8. DFS and BFS Graph Traversals (`practical-08-dfs-bfs`)

| Algorithm | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **DFS** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ worst case | Depth-first traversal using an explicit stack |
| **BFS** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ worst case | Breadth-first traversal using a queue |

### 9. Prim's Algorithm (`practical-09-prims-algorithm`)

| Algorithm | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Prim's Algorithm** | $\mathcal{O}(V^2)$ | $\mathcal{O}(V)$ | Greedy MST; grows the tree one vertex at a time (adjacency matrix) |

### 10. Kruskal's Algorithm (`practical-10-kruskals-algorithm`)

| Algorithm | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Kruskal's Algorithm** | $\mathcal{O}(E \log E)$ | $\mathcal{O}(V + E)$ | Greedy MST; picks cheapest edges avoiding cycles using Union-Find |

### 11. Floyd-Warshall Algorithm (`practical-11-floyd-warshall`)

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Dynamic Programming** | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^2)$ | Finds shortest distance between every pair of vertices |

### 12. Travelling Salesman Problem (`practical-12-travelling-salesman`)

| Approach | Time Complexity | Space Complexity | Description |
| :--- | :---: | :---: | :--- |
| **Held-Karp Dynamic Programming** | $\mathcal{O}(n^2 \cdot 2^n)$ | $\mathcal{O}(n \cdot 2^n)$ | Computes the minimum-cost tour visiting every city once |

---

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/gnaneswar449/DAA-practicals.git
   cd DAA-practicals
   ```

2. Run any sorting algorithm (e.g., Quick Sort):
   ```bash
   python practical-01-sorting-algorithms/quicksort.py
   ```

3. Run any searching algorithm (e.g., Binary Search):
   ```bash
   python practical-02-searching-algorithms/binary_search.py
   ```

4. Run Max Heap operations (Practical 03):
   ```bash
   python practical-03-max-heap/max_heap.py
   ```
5. Run the factorial comparison (Practical 04):
   ```bash
   python practical-04-factorial-comparison/factorial_comparison.py
   ```

6. Run the 0/1 knapsack dynamic programming solution (Practical 05):
   ```bash
   python practical-05-knapsack-dp/knapsack_dp.py
   ```

7. Run the matrix chain multiplication dynamic programming solution (Practical 06):
   ```bash
   python practical-06-matrix-chain-multiplication/matrix_chain_multiplication.py
   ```

8. Run the coin change dynamic programming solution (Practical 07):
   ```bash
   python practical-07-coin-change-dp/coin_change_dp.py
   ```

9. Run the DFS and BFS graph traversal solutions (Practical 08):
   ```bash
   python practical-08-dfs-bfs/dfs.py
   python practical-08-dfs-bfs/bfs.py
   ```

10. Run Prim's Algorithm MST solution (Practical 09):
    ```bash
    python practical-09-prims-algorithm/prims_algorithm.py
    ```

11. Run Kruskal's Algorithm MST solution (Practical 10):
    ```bash
    python practical-10-kruskals-algorithm/kruskals_algorithm.py
    ```

12. Run the Floyd-Warshall all-pairs shortest paths solution (Practical 11):
    ```bash
    python practical-11-floyd-warshall/floyd_warshall.py
    ```

13. Run the Travelling Salesman solution (Practical 12):
    ```bash
    python practical-12-travelling-salesman/travelling_salesman.py
    ```

---

## 👨‍💻 Author

**Gnaneswar Vuyyuri**  
- GitHub: [@gnaneswar449](https://github.com/gnaneswar449)
- Email: vuyyurignaneswar90@gmail.com
