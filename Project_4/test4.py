password = input("请输入密码：")
jud = True
jud_num = False
jud_alpha = False

while True:
    if not password[0].isupper():
        jud = False
        break
    for char in password:
        if not jud_num and char.isdigit():
            jud_num = True
        if not jud_alpha and char.isalpha():
            jud_alpha = True
        if not (char.isalpha() or char.isdigit()):
            jud = False
            break
    break

if jud and jud_num and jud_alpha:
    print("您的输入合法")
else:
    print("您的输入不合法")