num = -1
num_list = []
while True:
    num = input("请连续输入整数：")
    if num == '':
        break
    else:
        num_list.append(num)

list_1 = [int(x) for x in num_list if int(x) < 0]
list_2 = [int(x) for x in num_list if int(x) == 0]
list_3 = [int(x) for x in num_list if int(x) > 0]

for num in list_1:
    print(num,end=' ')
for num in list_2:
    print(num,end=' ')
for num in list_3:
    print(num,end=' ')