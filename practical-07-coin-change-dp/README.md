# Practical 7: Coin Change Problem using Dynamic Programming

This practical demonstrates the **Coin Change Problem** using **Dynamic Programming (DP)**. The program finds the minimum number of coins needed to make a given amount using a specified set of coin denominations.

---

## Problem Statement

Given a set of coin denominations and a target amount, determine the minimum number of coins required to form that amount. If the amount cannot be formed, print that it is not possible.

This solution uses **dynamic programming** to avoid repeated work and improve efficiency.

---

## Key Idea

Dynamic programming builds the answer for smaller amounts first and then uses those results to compute larger amounts.

If `dp[x]` represents the minimum number of coins required to make amount `x`, then:

`dp[x] = min(dp[x], dp[x - coin] + 1)`

for every valid coin denomination.

---

## Time and Space Complexity

| Approach | Time Complexity | Space Complexity |
| :--- | :---: | :---: |
| Dynamic Programming | $O(amount \times number\_of\_coins)$ | $O(amount)$ |

This is efficient compared to the brute-force recursive method, which repeats many subproblems.

---

## Python Program

```python
import time


def min_coins_dynamic_programming(coins, amount):
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
```

---

## Example Output

```text
Dynamic Programming - Minimum Coin Change Problem
------------------------------------------------
Enter coin denominations separated by spaces: 1 2 5
Enter the target amount: 11

--- Results ---
Coin denominations: [1, 2, 5]
Target amount: 11
Minimum number of coins required: 3
Execution Time: 0.000001500 seconds
```

---

## How to Run

```bash
cd practical-07-coin-change-dp
python coin_change_dp.py
```

---

## Author

**Gnaneswar Vuyyuri**
