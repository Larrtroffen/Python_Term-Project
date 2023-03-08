# 15_1-10000的完美数
print('1-10000的完美数有：')
# 依次遍历1-10000  
for num in range(1,10001):
    # 初始化累加和
    sum = 0
    # 遍历因子数并累加
    for i in range(1,num):
        if num % i == 0:
            sum += i
    # 判断累加和是否等于本身
    if sum == num:
        print(num)