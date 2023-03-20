# 获取两个字符串中不同的字符
# 方法一：
# a = input('1请输入：')
# b = input('2请输入：')
# for i in range(0, len(a)):
#     if a[i] == b:
#         continue
#     else:
#         print(a[i])
# for i in range(len(a), len(b)):
#     if b[i] == a:
#         continue
#     else:
#         print(b[i])
# 方法二：
import difflib
a = input('请输入')
b = input('请输入')
d = difflib.Differ()
diff = d.compare(a.splitlines(), b.splitlines())
print('\n'.join(list(diff)))
