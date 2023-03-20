# 输入密码，判断密码是否符合要求(密码中只能由数字和字母组成)
s = input('请输入密码')
for c in s:
    if c in '0123456789abcdefghejklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        continue
    else:
        print('False密码格式错误')
        break
