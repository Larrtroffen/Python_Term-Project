# 输入30个数字，并计算平均数
numbers = []
for i in range(30):
    num = float(input("Enter a number: "))
    numbers.append(num)
average = sum(numbers) / len(numbers)
print("The average is:", average)

