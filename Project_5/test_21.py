# 练习21
lstA = [10,20,30,40,50]
lstB = [100,200,300]
def combination(lstA,lstB):
    lst = []
    for i in range(max(len(lstA),len(lstB))):
        if lstA:
            lst.append(lstA[i])
        if lstB:
            if i < len(lstB):
                lst.append(lstB[i])
            else:
                continue
    return lst

print(combination(lstA,lstB))