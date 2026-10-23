import time


def min_coins_dynamic_programming(coins, amount):
    """Returns the minimum number of coins needed to make the amount using DP."""
    if amount < 0:
        return -1
    if amount == 0:
        return 0

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for target in range(1, amount + 1):
        for coin in coins:
            if coin <= target and dp[target - coin] != float('inf'):
                dp[target] = min(dp[target], dp[target - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def main():
    print("Dynamic Programming - Minimum Coin Change Problem")
    print("------------------------------------------------")

    try:
        coin_input = input("Enter coin denominations separated by spaces: ")
        coins = list(map(int, coin_input.split()))
        if not coins:
            raise ValueError

        for coin in coins:
            if coin <= 0:
                raise ValueError

        amount = int(input("Enter the target amount: "))
        if amount < 0:
            raise ValueError

    except ValueError:
        print("Invalid input! Please enter positive coin values and a non-negative amount.")
        return

    start_time = time.perf_counter()
    result = min_coins_dynamic_programming(coins, amount)
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print("\n--- Results ---")
    print(f"Coin denominations: {coins}")
    print(f"Target amount: {amount}")

    if result == -1:
        print("Minimum number of coins required: Not possible")
    else:
        print(f"Minimum number of coins required: {result}")

    print(f"Execution Time: {execution_time:.9f} seconds")


if __name__ == "__main__":
    main()
