def factorial_recursive(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_tail(n, acc=1):
    if n == 0 or n == 1:
        return acc
    return factorial_tail(n - 1, n * acc)


def fibonacci_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    print("Factorial(5) Recursive:", factorial_recursive(5))
    print("Factorial(5) Tail-Recursive:", factorial_tail(5))
    print("Fibonacci series (first 8 terms):", [fibonacci_recursive(i) for i in range(8)])