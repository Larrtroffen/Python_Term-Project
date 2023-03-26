# 练习18

def modify(lst):
    lst1 = []
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    print("去重之后",lst)
    lst1.sort(reverse=True)
    print("倒序排序",lst)
    return

lst = [70,88,91,70,107,234,91,177,282,197]
modify(lst)