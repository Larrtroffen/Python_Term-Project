# 计算BMI
try:
    height = float(input())
    weight = float(input())
    if height < 1.2 or height > 2.3:
        print("身高输入有误")
    elif weight < 20 or weight > 200:
        print("体重输入有误")
    else:    
        bmi = weight / (height * height)
        print("BMI是：")
        print('%.1f' % bmi)
except:
    print("输入有误")