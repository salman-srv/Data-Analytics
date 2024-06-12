def compress_string(s):
    compressed = ""
    c_count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            c_count += 1
        else:
            compressed += s[i - 1] + str(c_count)
            c_count = 1
    compressed += s[-1] + str(c_count)
    if len(compressed) >= len(s):
        return s
    else:
        return compressed

s = str(input(""))
r = compress_string(s)
print(r)
