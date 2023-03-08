# 字母映射到绩点
try:
    level = str(input())
except:
    print("输入有误！")
if level == "A+":
    print("4.0")
elif level == "A":
    print("4.0")
elif level == "A-":
    print("3.7")
elif level == "B+":
    print("3.3")
elif level == "B":
    print("3.0")
elif level == "B-":
    print("2.7")
elif level == "C+":
    print("2.3")
elif level == "C":
    print("2.0")
elif level == "C-":
    print("1.7")
elif level == "D+":
    print("1.3")
elif level == "D":
    print("1.0")
elif level == "F":
    print("0")
else:
    print("输入错误")