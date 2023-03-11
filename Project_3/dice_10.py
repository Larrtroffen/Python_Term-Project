# 10_骰子
import random

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += random.randint(1, 6)
    return total

n = input("请输入骰子的个数：")
print(roll_dice(n))