# 确定元素个数
# 它确定并返回列表中大于或等于某个最小值而小于某个最大值的元素数。
# 函数接收三个参数:列表、最小值和最大值。
ls = []
s = input('请输入列表:')
ls = s.split()
ma = input('请输入最大值：')
mi = input('请输入最小值：')
def countRange():
    ls1 = [x for x in ls if (x >= mi)and(x < ma)]
    return len(ls1)
print(countRange())