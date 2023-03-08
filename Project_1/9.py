# 判断整数奇偶
try:
    num = int(input())
    if num % 2 == 0:
        print("偶数")
    else:
        print("奇数")
except:
    print("输入的不是整数！")    