from functools import cache


def fib(n):
    """
    Naive fibonacci implementation.

    Since it uses recursion, it is not efficient.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


memo = {}


def memoised_fib(n):
    """
    Memoised fibonacci implementation.

    Memoisation is a technique to store the results of expensive computations
    in an external data structure.

    By doing so, we only need to compute each fibonacci number once
    and reuse the results. We are basically trading space for time.
    """
    if n not in memo:
        memo[n] = fib(n)
    return memo[n]


@cache
def cached_fib(n):
    """
    You may also create a cached function by using @cache.

    Cache and Memoisations are synonyms.
    """
    return fib(n)
