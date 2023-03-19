# 练习8
def nonum(str):
    sum = 0
    for i in str:
        if i.isdigit() == False:
            sum += 1
    return sum

str = input('请输入字符串')
print(nonum(str))
            