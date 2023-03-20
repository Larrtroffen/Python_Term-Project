# 练习9
def sorted_(lst):
    lst1 = lst.sort()
    lst2 = lst.sort(reverse=False)
    if lst == lst1:
        return True
    elif lst == lst2:
        return True
    else:
        return False
    
lst = [2,3,4,5,6,7,8]
print(sorted_(lst))