# 12_购物卡组合
for i in range(7):
    for j in range(51):
        for k in range(21):
            if i*15 + j*2 + k*5 == 100:
                print(f"洗发水{i}瓶,肥皂{j}块,牙刷{k}支")