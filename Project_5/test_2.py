num = -1
num_list = []

while True:
    num = int(input("请连续输入整数："))
    if num == 0:
        break
    else:
        num_list.append(num)

num_list.reverse()

for num in num_list:
    print(num)