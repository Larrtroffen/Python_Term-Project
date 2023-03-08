# 月名对应天数
try:
    month = int(input())
except:
    print("输入的不是整数！")
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30天")
elif month == 2:
    print("28天或29天")
else:
    print("输入的月份有误")