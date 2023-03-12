#  练习2：出租车费
def main():
    s = float(input('请输入旅行距离(单位为公里）'))
    f0 = 4.00
    i = s % 0.14
    m = s / 0.14
    if i == 0:
        f = f0 + m * 0.25
    else:
        f = f0 + (m + 1) * 0.25
    return f
if __name__ == '__main__':
    print('出租车车费为：', main())

