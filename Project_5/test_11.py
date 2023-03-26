def isSublist(larger:list,smaller:list):

    if not smaller:
        return True

    index = -1
    # 找到与smaller数组第一个值一样的larger数组的索引
    for i in larger:
        if i == smaller[0]:
            index = larger.index(i)
            break
    if index == -1:
        return False

    # 使用索引遍历smaller数组
    cnt = 0

    for num in range(index,len(larger)):
        if larger[num] != smaller[cnt]:
            return False
        # 防止越界
        if cnt<len(smaller) and (cnt+1)!=len(smaller):
            cnt += 1
        else:
            return True

if __name__ == '__main__':
    print(isSublist([1, 2, 3, 4, 'a', 'b'], [2, 4, 'a']))
    print(isSublist([1, 2, 3, 4, 'a', 'b'], []))
    print(isSublist([1, 2, 3, 4, 'a', 'b'], [8]))
    print(isSublist([1, 2, 3, 4, 'a', 'b'], [3, 4, 'a']))
