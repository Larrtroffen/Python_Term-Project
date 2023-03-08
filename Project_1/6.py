# 读取整数各数字的和
num = list(str(input()))
sum = 0
try:
    for i in num:
        i = int(i)
        sum += i
    print("整数各数字的和是：")
    print(sum)
except:
    print("输入的不是整数！")