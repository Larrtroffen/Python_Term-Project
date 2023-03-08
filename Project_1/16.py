# 出生日期到星座的对应
try:
    month = int(input())
    date = int(input())
except:
    print("输入的不是数字！")
if month == 1:
    if date < 20:
        print("摩羯座")
    else:
        print("水瓶座")
elif month == 2:
    if date < 19:
        print("水瓶座")
    else:
        print("双鱼座")
elif month == 3:
    if date < 21:
        print("双鱼座")
    else:
        print("白羊座")
elif month == 4:
    if date < 20:
        print("白羊座")
    else:
        print("金牛座")
elif month == 5:
    if date < 21:
        print("金牛座")
    else:
        print("双子座")
elif month == 6:
    if date < 22:
        print("双子座")
    else:
        print("巨蟹座")
elif month == 7:
    if date < 23:
        print("巨蟹座")
    else:
        print("狮子座")
elif month == 8:
    if date < 23:
        print("狮子座")
    else:
        print("处女座")
elif month == 9:
    if date < 23:
        print("处女座")
    else:
        print("天秤座")
elif month == 10:
    if date < 23:
        print("天秤座")
    else:
        print("天蝎座")
elif month == 11:
    if date < 22:
        print("天蝎座")
    else:
        print("射手座")
elif month == 12:
    if date < 22:
        print("射手座")
    else:
        print("摩羯座")
else:
    print("输入有误！")