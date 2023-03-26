# 避免重复
ls = []
ls1 = []
w = input('请输入单词：')
ls = w.split()
for i in range(0, len(ls)):
    p = ls.pop()
    if p in ls:
        ls1 = ls1
    else:
        ls1.append(p)
print(ls1)
