# 4_随机车牌
# 在一个特定的司法管辖区,旧的车牌由三个字母和三个数字组成。当所有遵
# 循该模式的牌照被使用后，车牌的格式更改为四个数字后面跟着三个字母。
# 编写一个函数，生成随机的车牌。函数为旧车牌或新车牌生成字母序列的概
# 率应该大致相等。编写一个 main 程序，调用函数并显示随机生成的车牌。
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

