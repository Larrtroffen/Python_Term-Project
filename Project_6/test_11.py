# 练习11
import random
A = set()
B = set(random.sample(range(10000), 1000))
C = set(random.sample(range(8000, 10000), 1000))

B_C_intersection = B.intersection(C)
print(B_C_intersection)

B_C_union = B.union(C)
print(B_C_union)

B_C_difference = B.difference(C)
print(B_C_difference)

C_B_difference = C.difference(B)
print(C_B_difference)
