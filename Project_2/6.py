# 6_乘法表

# 按列输出
for i in range(1,11):
    # 按行输出
    for j in range(1,11):
        # 每行第一个数字输出列数
        if j == 1:
            print(f"{i}",end='\t')
        # 每行第二个数字输出列数乘以行数
        print(f"{i*j}",end='\t')
    # 每行输出完换行
    if j == 10:
        print("\n")