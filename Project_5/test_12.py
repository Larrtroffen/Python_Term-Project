# 练习12
def find_sublists(lst):
    result = [[]]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            result.append(lst[i:j])
    return result

lst = [1,2,3,4,5]
print(find_sublists(lst))