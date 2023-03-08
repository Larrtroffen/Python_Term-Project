# 9_整数中各数字的和
print("请输入一个整数,该程序可以计算该整数中各位数的和\n输入为空时停止该程序。")
while True:
    # 请求输入一个整数
    print("请输入:")
    num = input()
    # 输入空白行结束循环
    if num == '':
        print("程序结束")
        break
    # 初始化累加和
    sum = 0
    # 遍历整数中的每个数字并累加
    try:
        for i in num:
            sum += int(i)
    except:
        print("输入错误")
        exit()
    print("该整数中各位数的和为:")
    print(sum)