# 求出100~200之间不能被3整除的整数，要求以每行5个数字的格式输出。（提示：使用列表来保存结果）
ls = []
for a in range(100, 201):
    if a % 3 != 0:
        ls.append(a)
    else:
        continue
for i in range(0, len(ls)):
    if (i+1) % 5 == 0:
        print(ls[i-5: i])