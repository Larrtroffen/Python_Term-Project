# 练习一：求平均值——两种方法
# 方法一
# lst = []  # 空列表
# lst2 = []
# str = input('请输入')
# lst1 = str.split(' ')  # 将字符串按空格分割成列表
# for num in lst1:
#     lst.append(float(num))  # 将字符串列表中的元素转换为浮点数并添加到lst中

# if len(lst) == 0 or lst[0] == 0:  # 如果lst为空或第一个元素为0，则无法计算平均值
#     print('您可能出错啦')
# else:
#     for i in range(0, len(lst)):
#         if lst[i] == 0:
#             lst2 = lst[0:i]  # 注意是lst而不是lst1
#             break
#         else:
#             lst2 = lst

# def add():
#     s = sum(lst2)
#     return s

# def average():
#     if len(lst2) == 0:  # 防止除数为0
#         return 0
#     avg = add() / len(lst2)
#     return avg
# print('avg = %f' % average())

#方法二：
sum = 0
i = 0
while True:
    str = input('请输入')
    if str == '0' and i == 0:
        print('您可能出错啦')
        break
    elif str == '0':
        print('avg = % f' % (sum / i))
        break
    else:
        sum += float(str)
        i += 1
