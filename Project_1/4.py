import math
# 自由落体运动计算速度
vi = 0
a = 9.8
try:
    height = float(input())
    vf = math.sqrt(vi * vi + 2 * a * height)
    print("自由落体运动的速度是：")
    print('%.1f' % vf)
except:
    print("输入的高度有误！")