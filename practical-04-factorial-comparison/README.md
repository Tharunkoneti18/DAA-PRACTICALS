# Practical 4: Factorial Calculation using Iteration and Recursion

This practical demonstrates two ways to compute the factorial of a non-negative integer:

1. **Iterative method** using a loop
2. **Recursive method** using function calls

The program also measures the execution time of both implementations and compares their results.

---

## Problem Statement

Write a program to calculate the factorial of a number using:
- an iterative approach
- a recursive approach

Also show the time taken by both methods for the same input.

---

## Time and Space Complexity

| Method | Time Complexity | Space Complexity |
| :--- | :---: | :---: |
| Iterative Factorial | $O(n)$ | $O(1)$ |
| Recursive Factorial | $O(n)$ | $O(n)$ |

- The iterative method uses a loop and no additional stack memory.
- The recursive method uses the function call stack, so its space complexity is higher.

---

## Python Program

```python
import time


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    while True:
        try:
            n = int(input("Enter a non-negative integer (for example, 10): "))
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Please enter a non-negative integer.")

    start_time = time.perf_counter()
    iterative_result = factorial_iterative(n)
    end_time = time.perf_counter()
    iterative_time = end_time - start_time

    start_time = time.perf_counter()
    recursive_result = factorial_recursive(n)
    end_time = time.perf_counter()
    recursive_time = end_time - start_time

    print(f"\n--- Results for {n}! ---")
    print(f"Iterative Result : {iterative_result}")
    print(f"Iterative Time   : {iterative_time:.9f} seconds")
    print("-------------------------------")
    print(f"Recursive Result : {recursive_result}")
    print(f"Recursive Time   : {recursive_time:.9f} seconds")


if __name__ == "__main__":
    main()
```

---

## Example Output

```text
Enter a non-negative integer (for example, 10): 5

--- Results for 5! ---
Iterative Result : 120
Iterative Time   : 0.000000500 seconds
-------------------------------
Recursive Result : 120
Recursive Time   : 0.000000700 seconds
```

---

## How to Run

```bash
cd practical-04-factorial-comparison
python factorial_comparison.py
```

---

## Author

**Gnaneswar Vuyyuri**
