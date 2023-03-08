# 练习8
# 1
ans1 = 0
for i in range(1, 101):
    ans1 += i
print(ans1)

ans2 = 0
i = 1
while i <= 100:
    ans2 += i
    i += 1
print(ans2)

# 2
ans3 = 0
jud = True
for i in range(1,100,2):
    if jud:
        ans3+=i
        jud = False
    else:
        ans3-=i
        jud = True
print(ans3)

# 3
ans4 = 0
for i in range(0,991,10):
    ans4+=i+6
print(ans4)

# 4
for i in range(5):
    for j in range(4 - i):
        print(" ", end="")
    for k in range(i * 2 + 1):
        print("*", end="")
    print()
# 5
def compute(num1,num2,strs):
    ans = None
    if strs == "+":
        ans = num1 + num2
    elif strs == "-":
        ans = num1 - num2
    elif strs == "*":
        ans = num1 * num2
    elif strs == "/":
        if num2 != 0:
            ans = num1 / num2
    return ans

num1 = float(input("请输入第一个数字:"))
num2 = float(input("请输入第二个数字:"))
strs = input("请输入运算符:")
ans6 = compute(num1,num2,strs)
if ans6 is not None:
    print(ans6)
else:
    print("您输入的除数或者运算符有误")