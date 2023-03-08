# 计算第二天
try:
    year = int(input())
    month = int(input())
    date = int(input())
except:
    print("输入的不是数字！")
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if date == 31:
        if month == 12:
            print(year + 1, 1, 1)
        else:
            print(year, month + 1, 1)
    else:
        print(year, month, date + 1)
elif month == 4 or month == 6 or month == 9 or month == 11:
    if date == 30:
        if month == 12:
            print(year + 1, 1, 1)
        else:
            print(year, month + 1, 1)
    else:
        print(year, month, date + 1)
elif month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if date == 29:
            print(year, month + 1, 1)
        else:
            print(year, month, date + 1)
else:
    print("输入错误")