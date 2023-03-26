# 利用列表推导式将列表中的整数提取出来
ls1 = [x for x in [True, 17, 'hello', 'bye', 98, 34, 12] if type(x) == int]
print(ls1)
