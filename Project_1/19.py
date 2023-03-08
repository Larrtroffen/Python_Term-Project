# 解决四舍五入的问题
import bisect
import math

def solve(num):
    strs = str(num)
    if int(strs[3]) >= 5:
        return float(strs[:3]) + 0.1
    else:
        return float(strs[:3])

try:
    num = input("请输入您的绩点:")

    if len(num) > 3:
        num = solve(num)
    num = float(num)

    if num in range(4,5):
        print("A+")
        
    if num < 0 or num > 5:
        print("输入错误!")
        
    else:
        strs = ["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","F"]
        grades = [4.0,4.0,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.3,1.0,0]
        # [0, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 4.0]
        strs.reverse()
        grades.reverse()

        pos = bisect.bisect(grades,num)
        # print(len(grades))
        # print(pos)
        if math.fabs(num-grades[pos]) >= math.fabs(num-grades[pos-1]):
            print(strs[pos-1])
        else:
            print(strs[pos])
except:
    print("输入有误！")