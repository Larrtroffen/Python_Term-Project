# 练习11
def find_index(str1,str2):
    found = False
    for i in range(len(str1)):
        if str1[i:i+len(str2)] == str2:
            found = True
            return i
    if not found:
        return '未找到'

str1 = input('请输入大字符串')
str2 = input('请输入要寻找的字符串')
print(find_index(str1,str2))

