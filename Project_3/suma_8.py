# 练习8：把这些值加起来
def suma():
    s = input('请输入数值')
    if s == '':
        return 0.0
    else:
        return float(s) + suma()
sumt = suma()
print(sumt)
