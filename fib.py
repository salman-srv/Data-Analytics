def fibonacci(n):
    fib_series = []
    if n <= 0:
        return fib_series
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
n = int(input())
fib_numbers = fibonacci(n)
print(" ".join(map(str, fib_numbers)))
