# 获取两个列表中元素相同
def same():
    A = [9, 0, 7, 8, 'hello']
    B = [8, 'hello', 99, 0, 2]
    print([x for x in A if x in B])
same()