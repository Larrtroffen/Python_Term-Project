# 季节的确定日期
try:
    month = str(input())
    date = int(input())
except:
    print("输入的不是数字！")
if month == "一月":
    print("冬季")
elif month == "二月":
    print("冬季")
elif month == "三月":
    if date < 20:
        print("冬季")
    else:
        print("春季")
elif month == "四月":
    print("春季")
elif month == "五月":
    print("春季")
elif month == "六月":
    if date < 21:
        print("春季")
    else:
        print("夏季")
elif month == "七月":
    print("夏季")
elif month == "八月":
    print("夏季")
elif month == "九月":
    if date < 22:
        print("夏季")
    else:
        print("秋季")
elif month == "十月":
    print("秋季")
elif month == "十一月":
    print("秋季")
elif month == "十二月":
    if date < 21:
        print("秋季")
    else:
        print("冬季")
else:
    print("输入有误！")