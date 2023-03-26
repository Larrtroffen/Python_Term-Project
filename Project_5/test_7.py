# 只看单词
ls1 = []
def word():
    s = input('请输入单词')
    ls = s.split()
    for i in range(0, len(ls)):
        w = ls.pop()
        wo = w.strip(",.?!:;'")
        ls1.append(wo)
    return ls1[::-1]
print(word())
