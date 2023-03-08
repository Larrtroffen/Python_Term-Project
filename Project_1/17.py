# 生肖判断
try:
    year = int(input())
except:
    print("输入的不是数字！")
if year % 12 == 0:
    print("猴")
elif year % 12 == 1:
    print("鸡")
elif year % 12 == 2:
    print("狗")
elif year % 12 == 3:
    print("猪")
elif year % 12 == 4:
    print("鼠")
elif year % 12 == 5:
    print("牛")
elif year % 12 == 6:
    print("虎")
elif year % 12 == 7:
    print("兔")
elif year % 12 == 8:
    print("龙")
elif year % 12 == 9:
    print("蛇")
elif year % 12 == 10:
    print("马")
elif year % 12 == 11:
    print("羊")
elif year % 12 == 12:
    print("猴")
else:
    print("输入有误！")