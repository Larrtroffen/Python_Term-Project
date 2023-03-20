# 练习3
def remove_extreme_values(lst, n):
    if len(lst) < 2*n:
        return '输入错误'
    sorted_lst = sorted(lst)
    return sorted_lst[n:len(lst)-n]

def main():
    lst = []
    while True:
        i = input('请输入一个数字，到空格停止')
        if i == '':
            break
        else:
            i = int(i)
            lst.append(i)
    print(remove_extreme_values(lst,2))
    return lst

print(main())

