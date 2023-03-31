# 练习5
str1 = input("请输入第一个字符串：")
str2 = input("请输入第二个字符串：")

if sorted(str1) == sorted(str2):
    print("是字谜")
else:
    print("不是字谜")
