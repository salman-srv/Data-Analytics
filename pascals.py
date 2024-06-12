from math import factorial
num_rows = int(input())
pascals_triangle = []
for n in range(num_rows):
    row_values = []
    for r in range(n + 1):
        ncr = factorial(n) // (factorial(r) * factorial(n - r))
        row_values.append(ncr)
    pascals_triangle.append(row_values)

print(pascals_triangle)
