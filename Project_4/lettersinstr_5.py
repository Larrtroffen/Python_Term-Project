# 练习5
def lis(str):
    str1 = ''.join([i for i in str if i.isalpha()])
    return str1

str = input('请输入字符串')
print(lis(str))