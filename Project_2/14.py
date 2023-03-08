# 练习14
for i in range(3):
    password = input("请正确输入密码，您已经输入{}次，最多三次：".format(i))
    if password == '111111':
        amount = float(input("请输入取款金额，最低100，最高1000："))
        while True:
            if amount % 100 == 0 and 100 <= amount <= 1000:
                print("取款成功，取走{}".format(amount))
                print("交易完成，请取卡")
                break
            else:
                amount = float(input("请重新输入取款金额，最低100，最高1000："))
        break
    elif i==2 and password != '111111':
        print("密码错误，请取卡")
    else:
        print("密码错误")