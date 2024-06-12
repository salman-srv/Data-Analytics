def freq_sort(nums):
    freq_dict = {}
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    sorted_nums = sorted(nums, key=lambda x: (freq_dict[x], -x))
    return sorted_nums

input_str = input()
nums = list(map(int, input_str.split()))
result = freq_sort(nums)
print(result)
