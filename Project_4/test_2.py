# 练习2
def pwd(password):
    if len(password) in range(6,10):
        return '密码合法'
    else:
        return '密码不合法'
    
password = input('请输入密码')
print(pwd(password))