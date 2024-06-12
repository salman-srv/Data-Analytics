def max_distance(arr):
    max_dist = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                max_dist = max(max_dist, j - i)
    return max_dist

input_str = input("")
arr = list(map(int, input_str.split()))
result = max_distance(arr)
print(result)
