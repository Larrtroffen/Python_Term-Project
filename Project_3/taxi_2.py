#  练习2：出租车费
def fee():
    s = float(input('请输入旅行距离(单位为公里）'))
    f0 = 4.00
    f1 = 0.25
    if s <= 0.14:
        f = f0
    else:
        f = f0 + (s - 0.14) / 0.14 * f1
    return f
print(fee())
