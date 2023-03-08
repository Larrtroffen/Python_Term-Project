# 摄氏温度转换为华氏温度
try:
    cel = float(input())
    fah = cel * 1.8 + 32
    k = cel + 273.15
    print("华氏温度是：")
    print('%.1f' % fah)
    print("开氏温度是：")
    print('%.1f' % k)
except:
    print("输入有误")