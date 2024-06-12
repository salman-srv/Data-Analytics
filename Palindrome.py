def is_palindrome():
    s = str(input())
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(is_palindrome())
