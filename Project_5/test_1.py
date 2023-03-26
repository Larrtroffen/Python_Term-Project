# 升序排列,0终止输入
sl = []
while True:
    s = input('请输入整数')
    if s == '0':
        break
    else:
        sl.append(s)
sl1 = sorted(sl)
print(sl1)
