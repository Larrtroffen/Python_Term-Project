# 练习9
def sorted_(lst):
    return sorted(lst) == lst or sorted(lst, reverse=True) == lst
    
lst = [2,3,4,5,6,7,8]
print(sorted_(lst))