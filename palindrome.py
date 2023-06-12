def is_palindrome(s):
    return s == s[::-1]

s = input()
print(is_palindrome(s))