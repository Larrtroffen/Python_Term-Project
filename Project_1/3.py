import math
# 计算圆柱体体积
try:
    round = float(input())
    height = float(input())
    s = round * round * math.pi
    v = s * height
    print("圆柱体的体积是：")
    print('%.1f' % v)
except:
    print("输入的不是数字！")