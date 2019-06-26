def fib(n):
    return n if (n == 1 or n == 0) else (n + fib(n-1))
