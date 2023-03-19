def is_palindrome(name):
    return name == name[::1]

name1 = str(input())
print(is_palindrome(name1))