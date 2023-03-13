# 练习9

def calculate(a,b):
    if b == 0:
        return a
    else:
        c = a%b
        return calculate(b,c)


num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))
print(calculate(num1,num2))
