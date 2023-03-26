# 5个整数，最小值与第一个元素调换，输出
lst = []
while True:
    s = int(input('请依次输入5个整数'))
    lst.append(s)
    if len(lst) == 5:
        break

def change_position(lst):
    i = lst.index(min(lst))
    lst[0],lst[i]=lst[i],lst[0]
    return lst

print(change_position(lst))
