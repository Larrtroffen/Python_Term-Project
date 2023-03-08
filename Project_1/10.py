# 判断元音或辅音
try:
    input = str(input())
    if input == "a" or input == "e" or input == "i" or input == "o" or input == "u":
        print("元音")
    elif input == "y":
        print("有时元音，有时辅音")
    else:
        print("辅音")
except:
    print("输入的不是字母！")