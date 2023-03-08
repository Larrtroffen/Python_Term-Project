import math
# 求正多边形的面积
try:
    side = float(input())
    n = int(input())
    if n < 3:
        print("边数不能小于3")
    else:
        area = n * side * side / (4 * (math.pi / n))
        print("正多边形的面积是：")
        print('%.2f' % area)
except:
    print("输入有误")