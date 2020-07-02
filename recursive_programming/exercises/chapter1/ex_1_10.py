from math import sqrt

# pylint: disable=invalid-name
# 1. Implement fibonacci using linear recursion

GOLDEN_RATION = (1 + sqrt(5)) / 2


def fib_linear_recursion(n: int) -> int:
    if n in [1, 2]:
        return 1
    return int(GOLDEN_RATION * fib_linear_recursion(n - 1) + 0.5)


print(f"Solving Fibonacci using Linear Recursion, F(10) = {fib_linear_recursion(10)}")


# 2. Tail recursion
def fib_tail_recursion(n: int) -> int:
    def fib_helper(n: int, current: int = 1, prev: int = 1) -> int:
        if n == 0:
            return current

        return fib_helper(n - 1, current + prev, current)

    return 1 if (n == 1 or n == 2) else fib_helper(n - 2)


print(f"Solving Fibonacci using Tail Recursion, F(10) = {fib_tail_recursion(10)}")

# 3. Multiple recursion


def fib_multiple_recursion(n: int) -> int:
    if n in [1, 2]:
        return 1
    elif n % 2 == 0:
        return (fib_multiple_recursion(n // 2 + 1) ** 2) - (
            fib_multiple_recursion(n // 2 - 1) ** 2
        )
    else:
        return (fib_multiple_recursion((n + 1) // 2) ** 2) + (
            fib_multiple_recursion((n - 1) // 2) ** 2
        )


print(
    f"Solving Fibonacci using Multiple Recursion, F(10) = {fib_multiple_recursion(10)}"
)

# 4. Mutual recursion


def fib_mutual_recursion(n: int) -> int:
    return fib_helper_b(n) + fib_helper_a(n)


def fib_helper_a(n: int) -> int:
    if n == 1:
        return 0
    return fib_helper_a(n - 1) + fib_helper_b(n - 1)


def fib_helper_b(n: int) -> int:
    if n == 1:
        return 1
    return fib_helper_a(n - 1)


print(
    f"Solving Fibonacci using Mutual/Indirect Recursion, F(10) = {fib_mutual_recursion(10)}"
)


# 5. Nested Recursion


def fib_nested_recursion(n: int) -> int:
    def fib_helper(n: int, s: int = 0) -> int:
        if n in [1, 2]:
            return 1 + s
        return fib_helper(n - 1, s + fib_helper(n - 2, 0))

    return fib_helper(n)


print(f"Solving Fibonacci using Nested Recursion, F(10) = {fib_nested_recursion(10)}")
