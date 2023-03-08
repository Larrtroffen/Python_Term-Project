# 二进制转换为十进制
# 方法一：
str = input('请输入数值:')
t = int(str, 2)
print('该数转化为十进制为：', t)

# 方法二：
lst = []
str = input('请输入数值：')
lst1 = str.split(' ')
for i in range(0, len(lst1)):
    lst.append(int(lst1.pop()))

