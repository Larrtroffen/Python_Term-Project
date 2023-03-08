import math
# 读取半径r
try:
    round = float(input())
    s = round * round * math.pi
    v = round * round * round * math.pi
    print("⚪的面积是：" + str(s) )
    print("⚪的体积是：" + str(v) )
except:
    print("输入的不是数字！")