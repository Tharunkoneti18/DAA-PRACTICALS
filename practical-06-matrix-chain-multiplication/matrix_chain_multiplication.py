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