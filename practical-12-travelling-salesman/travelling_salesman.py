import time

# Predefined distance matrix between cities - NO user input required.
# Cities: 0='A', 1='B', 2='C', 3='D', 4='E' (symmetric distances for undirected paths)
INF = float('inf')

dist = [
    [0, 20, 42, 35, 25],
    [20, 0, 30, 34, 16],
    [42, 30, 0, 12, 23],
    [35, 34, 12, 0, 18],
    [25, 16, 23, 18, 0],
]

cities = ['A', 'B', 'C', 'D', 'E']


def tsp_dynamic_programming(dist):
    """Returns the minimum tour cost and the optimal route using Held-Karp DP."""
    n = len(dist)
    num_masks = 1 << n

    # dp[mask][i] = minimum cost to start at city 0, visit exactly the cities
    # present in 'mask', and end at city i.
    dp = [[INF] * n for _ in range(num_masks)]
    parent = [[-1] * n for _ in range(num_masks)]

    dp[1][0] = 0   # start at city 0 (mask with only bit 0 set)

    for mask in range(num_masks):
        for last in range(n):
            if dp[mask][last] == INF:
                continue
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue   # city nxt is already visited
                new_mask = mask | (1 << nxt)
                new_cost = dp[mask][last] + dist[last][nxt]
                if new_cost < dp[new_mask][nxt]:
                    dp[new_mask][nxt] = new_cost
                    parent[new_mask][nxt] = last

    # Close the cycle by returning to the starting city 0
    full_mask = num_masks - 1
    best_cost = INF
    best_last = -1

    for last in range(1, n):
        cost = dp[full_mask][last] + dist[last][0]
        if cost < best_cost:
            best_cost = cost
            best_last = last

    # Reconstruct the optimal route
    route = []
    if best_last != -1:
        mask = full_mask
        node = best_last
        while mask > 1:
            route.append(node)
            prev = parent[mask][node]
            mask = mask & ~(1 << node)
            node = prev
        route.append(0)
        route.reverse()
        route.append(0)

    return best_cost, route


def main():
    print("Travelling Salesman Problem - Dynamic Programming (Held-Karp)")
    print("--------------------------------------------------------------")
    print("Distance matrix is predefined, NO user input required.\n")

    print("Distance matrix between cities:")
    for i in range(len(dist)):
        print(f"  {cities[i]}: {dist[i]}")

    start_time = time.perf_counter()
    min_cost, route = tsp_dynamic_programming(dist)
    end_time = time.perf_counter()

    print("\n--- Optimal Tour ---")
    print("Route:", " -> ".join(cities[c] for c in route))
    print(f"Minimum Tour Cost: {min_cost}")

    print("\n--- Time Complexity ---")
    print("Held-Karp Dynamic Programming: O(n^2 * 2^n)")

    print("\n--- Space Complexity ---")
    print("O(n * 2^n) for the DP table")

    print(f"\nExecution Time: {end_time - start_time:.9f} seconds")


if __name__ == "__main__":
    main()
