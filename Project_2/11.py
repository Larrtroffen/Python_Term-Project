# 练习11
def judge_num(num):
    judge = True
    for i in range(2,num):
        if num % i == 0:
            judge = False
            break
    return judge

cnt = 0
for i in range(101,201):
    if judge_num(i):
        cnt+=1
        print(i,end=" ")
print()
print(cnt)
