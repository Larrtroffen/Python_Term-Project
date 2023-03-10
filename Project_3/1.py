# 1_计算三角形斜边

# 输入两条直角边
side1 = float(input("请输入第一条直角边长: "))
side2 = float(input("请输入第二条直角边长: "))

# 使用勾股定理计算斜边
side3 = (side1 ** 2 + side2 ** 2) ** 0.5
print("斜边长为: ", side3)
