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