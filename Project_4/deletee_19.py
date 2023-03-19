# 练习19
def deletee(str):
    str1 = ''
    for i in str:
        if i != 'e':
            str1 += i
    return str1

str = input('请输入字符串')
print(deletee(str))