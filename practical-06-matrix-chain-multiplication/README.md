# Practical 6: Matrix Chain Multiplication using Dynamic Programming

This practical demonstrates the **Matrix Chain Multiplication Problem** using **Dynamic Programming (DP)**. Given a chain of matrices, the program finds the minimum number of scalar multiplications required to multiply the entire chain, by determining the optimal way to parenthesize the product.

---

## Problem Statement

Given `n` matrices and their dimensions, find the minimum number of scalar multiplications needed to multiply the whole chain.

Matrix multiplication is associative, so the product can be parenthesized in several ways. Different groupings can lead to different numbers of operations — the goal is to find the **optimal parenthesization** that minimizes the total cost.

---

## Key Idea

Let `p` be the array of dimensions such that matrix `Ai` has dimensions `p[i-1] x p[i]`. Let `dp[i][j]` represent the minimum number of multiplications needed to multiply matrices `Ai` through `Aj`.

For a chain of length ≥ 2, we split it at position `k` and take the minimum cost over all valid `k`:

```
dp[i][j] = min( dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1] )
```

where `dp[i][k]` and `dp[k + 1][j]` are the costs of the two sub-chains, and `p[i] * p[k + 1] * p[j + 1]` is the cost of multiplying the two resulting matrices.

The answer is stored in `dp[0][n - 1]`.

---

## Time and Space Complexity

| Approach | Time Complexity | Space Complexity |
| :--- | :---: | :---: |
| Dynamic Programming | $O(n^3)$ | $O(n^2)$ |

The triple nested loop over chain lengths, starting positions, and split positions gives the cubic time complexity. The DP table of size `n x n` gives the quadratic space complexity.

---

## Python Program

```python
import time

# Function for Matrix Chain Multiplication
def matrix_chain_order(p):
    n = len(p) - 1

    # DP table
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Chain length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            dp[i][j] = float('inf')

            # Try different positions to split the chain
            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# User input
n = int(input("Enter the number of matrices: "))

p = []

print("\nEnter the dimensions of the matrices:")

# First matrix dimensions
rows = int(input("Enter rows of Matrix 1: "))
cols = int(input("Enter columns of Matrix 1: "))

p.append(rows)
p.append(cols)

# Remaining matrices
for i in range(2, n + 1):
    rows = int(input(f"Enter rows of Matrix {i}: "))
    cols = int(input(f"Enter columns of Matrix {i}: "))

    # Check whether multiplication is possible
    if rows != p[-1]:
        print("Error: Matrix dimensions are not compatible.")
        exit()

    p.append(cols)


# Start execution timer
start_time = time.perf_counter()

# Calculate minimum multiplication cost
minimum_cost = matrix_chain_order(p)

# End execution timer
end_time = time.perf_counter()


# Display result
print("\n--- Matrix Chain Multiplication Result ---")
print("Minimum number of scalar multiplications:", minimum_cost)
print("Execution time:", end_time - start_time, "seconds")
```

---

## Example Output

```text
Enter the number of matrices: 3

Enter the dimensions of the matrices:
Enter rows of Matrix 1: 10
Enter columns of Matrix 1: 30
Enter rows of Matrix 2: 30
Enter columns of Matrix 2: 5
Enter rows of Matrix 3: 5
Enter columns of Matrix 3: 20

--- Matrix Chain Multiplication Result ---
Minimum number of scalar multiplications: 4500
Execution time: 1.8e-05 seconds
```

Here the matrices are `10x30`, `30x5`, and `5x20`. The optimal parenthesization `(A1 x A2) x A3` requires `10·30·5 + 10·5·20 = 1500 + 3000 = 4500` multiplications, which is less than `A1 x (A2 x A3)` at `30·5·20 + 10·30·20 = 3000 + 6000 = 9000`.

---

## How to Run

```bash
cd practical-06-matrix-chain-multiplication
python matrix_chain_multiplication.py
```

---

## Author

**Gnaneswar Vuyyuri**