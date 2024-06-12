def reverse_string(s):
    reversed_str = ""
    for char in s[::-1]:
        reversed_str += char
    return reversed_str
s = str(input())
reversed_string = reverse_string(s)
print(reversed_string)
