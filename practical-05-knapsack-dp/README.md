# Practical 5: 0/1 Knapsack Problem using Dynamic Programming

This practical demonstrates the **0/1 Knapsack Problem** using **Dynamic Programming (DP)**. Given a set of items, each with a weight and a value, the program finds the maximum total value that can be carried in a knapsack of a fixed capacity.

---

## Problem Statement

Given `n` items, each with a weight and a value, and a knapsack with a given capacity, determine the maximum value that can be obtained by selecting a subset of items whose total weight does not exceed the capacity.

Each item can be selected **only once** (0/1 knapsack). This solution uses **dynamic programming** to build the answer incrementally.

---

## Key Idea

Let `dp[i][w]` represent the maximum value obtainable using the first `i` items with a knapsack capacity of `w`. For each item, we decide whether to **include** it or **exclude** it:

`dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])`

if the item fits (`weights[i - 1] <= w`), otherwise we skip it (`dp[i][w] = dp[i - 1][w]`).

The answer is stored in `dp[n][capacity]`.

---

## Time and Space Complexity

| Approach | Time Complexity | Space Complexity |
| :--- | :---: | :---: |
| Dynamic Programming | $O(n \times capacity)$ | $O(n \times capacity)$ |

This is efficient compared to the brute-force approach (enumerating all $2^n$ subsets), which is exponential.

---

## Python Program

```python
import time

# Function to solve 0/1 Knapsack using Dynamic Programming
def knapsack(weights, values, capacity):
    n = len(values)

    # DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# User input
n = int(input("Enter the number of items: "))

weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    value = int(input(f"Enter value of item {i + 1}: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("Enter the capacity of the knapsack: "))

# Start execution timer
start_time = time.perf_counter()

# Calculate maximum profit/value
max_value = knapsack(weights, values, capacity)

# End execution timer
end_time = time.perf_counter()

# Display result
print("\n--- Knapsack Result ---")
print("Maximum value:", max_value)
print("Execution time:", end_time - start_time, "seconds")
```

---

## Example Output

```text
Enter the number of items: 4
Enter weight of item 1: 2
Enter value of item 1: 3
Enter weight of item 2: 3
Enter value of item 2: 4
Enter weight of item 3: 4
Enter value of item 3: 5
Enter weight of item 4: 5
Enter value of item 4: 6
Enter the capacity of the knapsack: 5

--- Knapsack Result ---
Maximum value: 7
Execution time: 1.9e-05 seconds
```

---

## How to Run

```bash
cd practical-05-knapsack-dp
python knapsack_dp.py
```

---

## Author

**Gnaneswar Vuyyuri**