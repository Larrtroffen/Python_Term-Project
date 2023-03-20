# 练习4
password = input("请输入密码：")

is_valid = True
has_digit = False
has_uppercase = False

if not password[0].isupper():
    is_valid = False

for char in password:
    if char.isdigit():
        has_digit = True
    elif char.isupper():
        has_uppercase = True
    elif not char.islower():
        is_valid = False
        break

if is_valid and has_digit and has_uppercase:
    print("您的输入合法")
else:
    print("您的输入不合法")
