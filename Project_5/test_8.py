num = -1
num_list = []
sum_ans = 0

while True:
    num = input("请连续输入数字：")
    if num == '':
        break
    else:
        sum_ans+=float(num)
        num_list.append(float(num))

avg = sum_ans//len(num_list)

print(avg)

high_list = []
low_list = []

for i in num_list:
    if i > avg:
        high_list.append(i)
    elif i < avg:
        low_list.append(i)

avg_list = [num for num in num_list if num == avg]

print("所有低于平均值的数：",low_list)
print("所有等于平均值的数：",avg_list)
print("所有高于平均值的数：",high_list)
