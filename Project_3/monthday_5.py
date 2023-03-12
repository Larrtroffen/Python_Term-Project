# 练习5：一个月的天数
def main():
    year = int(input('请输入年份：'))
    month = int(input('请输入月份（1-12月）：'))
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            d = '29天'
        else:
            d = '28天'
    elif month in (4, 6, 9, 11):
        d = '30天'
    else:
        d = '31天'
    print('该月份的天数为', d)
if __name__ == '__main__':
    main()


