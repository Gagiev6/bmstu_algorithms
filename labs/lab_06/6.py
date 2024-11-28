def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def series_sum(x, n):
    if n == 0:
        return 0
    else:
        return series_sum(x, n - 1) + (x ** (n - 1)) / factorial(n - 1)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def series_sum(x, n):
    total_sum = 0
    for i in range(n):
        term = (x ** i) / factorial(i)
        total_sum += term
    return total_sum

import timeit
from functools import lru_cache

def series_sum_iterative(x, n):
    total_sum = 0
    for i in range(n):
        term = (x ** i) / factorial(i)
        total_sum += term
    return total_sum #n

def series_sum_recursive(x, n):
    if n == 0:
        return 0
    term = (x ** (n - 1)) / factorial(n - 1)
    return term + series_sum_recursive(x, n - 1) #e^n

def series_sum_memo(x, n, memo={}):
    if n == 0:
        return 0
    if (x, n) in memo:
        return memo[(x, n)]#n
    term = (x ** (n - 1)) / factorial(n - 1)
    result = term + series_sum_memo(x, n - 1, memo)
    memo[(x, n)] = result
    return result

@lru_cache(maxsize=None)
def series_sum_memo_decorator(x, n):
    if n == 0:
        return 0
    term = (x ** (n - 1)) / factorial(n - 1)
    return term + series_sum_memo_decorator(x, n - 1)


x = 2
n = 10

iterative_time = timeit.timeit(lambda: series_sum_iterative(x, n), number=1000)
recursive_time = timeit.timeit(lambda: series_sum_recursive(x, n), number=1000)
memo_time = timeit.timeit(lambda: series_sum_memo(x, n), number=1000)
memo_decorator_time = timeit.timeit(lambda: series_sum_memo_decorator(x, n), number=1000)

print(f"Итеративная реализация: {iterative_time} секунд")
print(f"Рекурсивная реализация: {recursive_time} секунд")
print(f"Рекурсивная реализация с мемоизацией вручную: {memo_time} секунд")
print(f"Рекурсивная реализация с мемоизацией декоратором: {memo_decorator_time} секунд")