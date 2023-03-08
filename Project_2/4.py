# Fizz-Buzz游戏——两种方法
# 方法一：
for x in range(1, 101):
    print("fizz"[x % 3*6::]+"buzz"[x % 5*6::] or x)  # 切片语法 [起始索引:结束索引:步长] 三个值可全为空

# 方法二：
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('fizzbuzz')
    elif x % 3 == 0:
        print('fizz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print(x)
