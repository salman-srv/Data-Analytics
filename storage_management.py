def cal(a, b):
    return (a + b - 1) // b
def Phone(N, K, M):
    total_memory = N * K
    if total_memory < M:
        return -1
    else:
        apps_to_delete = cal(M, K)
        return apps_to_delete
N = int(input())
K = int(input())
M = int(input())
result = Phone(N, K, M)
print(result)
