# 三角形的分类
try:
    side1 = float(input())
    side2 = float(input())
    side3 = float(input())
except:
    print("输入的不是数字！")
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 and side1 == side3:
        print("等边三角形")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("等腰三角形")
    else:
        print("一般三角形")
else:
    print("不能构成三角形")