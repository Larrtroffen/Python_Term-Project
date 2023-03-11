# 4_随机车牌
import random
def main():
    # 生成随机车牌
    old = random.randint(0, 1)
    if old == 1:
        plate = ''
        for i in range(3):
            plate += chr(random.randint(65, 90))
        for i in range(3):
            plate += str(random.randint(0, 9))
    else:
        plate = ''
        for i in range(4):
            plate += str(random.randint(0, 9))
        for i in range(3):
            plate += chr(random.randint(65, 90))
    print('车牌号为：', plate)
main()

