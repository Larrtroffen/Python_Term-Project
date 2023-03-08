# 练习2
print("Celsius",end=" ")
print("fahrenheit")
for c in range(0, 101, 10):
    f = c * 1.8 + 32
    print("{} {}".format(c,f))