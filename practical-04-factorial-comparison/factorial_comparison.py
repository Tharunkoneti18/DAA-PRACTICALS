import time


def factorial_iterative(n):
    """Compute factorial using an iterative loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Compute factorial using recursion."""
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
