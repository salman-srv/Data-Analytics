def count_vowels(s):
    v = ['a','e','i','o','u','A','E','I','O','U']
    v_count = 0
    for char in s:
        if char in v:
            v_count = v_count+1
    return v_count

s = str(input())
r = count_vowels(s)
print(r)
