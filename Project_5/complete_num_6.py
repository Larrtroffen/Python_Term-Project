# 练习6
def complete_num(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    # 判断累加和是否等于本身
    if sum == num:
        return True
    else:
        return False
    
for i in range(1,10000):
    if complete_num(i) == True:
        print(i)