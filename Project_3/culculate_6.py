# 练习6
def simple(numerator,denominator):
    num = calculate(numerator,denominator)
    num1 = numerator/num
    num2 = denominator/num
    return num1,num2

def calculate(a,b):
    if b == 0:
        return a
    else:
        c = a%b
        return calculate(b,c)

numerator = int(input("请输入分子："))
denominator = int(input("请输入分母："))
if denominator == 0:
    print("您的输入有误")
else:
    num1, num2 = simple(numerator, denominator)
    print("{}/{}".format(int(num1), int(num2)))