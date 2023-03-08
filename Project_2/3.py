# 3_票价
# 初始化总票价
sum = 0
# 每行输入一个年龄，依次运行整个while下语句，直到输入一个空白行，结束循环
while True:
    age_input = input()
    if age_input == '':
        break
    age = int(age_input)
    # 单个年龄分别计算票价
    if age < 2:
        price = 0.00
    elif age < 12:
        price = 14.00
    elif age < 65:
        price = 23.00
    elif age >= 65:
        price = 18.00
    # 单价累加
    sum += price
# 输出总票价
print('票价为%.2f美元'%sum)