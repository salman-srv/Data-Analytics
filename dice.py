def DiceProblem(N):
    if N < 1 or N > 6:
        return -1
    else:
        return 7 - N

N = int(input())
result = DiceProblem(N)
print(result)
