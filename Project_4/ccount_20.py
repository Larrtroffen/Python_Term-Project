# 练习20
def ccount(str):
    count = 0
    for i in str:
        if i == 'c':
            count += 1
        elif i == 'C':
            count += 1
    return count

str = input('请输入字符串')
print(ccount(str))