# 练习5
def lis(str):
    str1 = ''.join(filter(str.isalpha, str))
    return str1

str = input('请输入字符串')
print(lis(str))