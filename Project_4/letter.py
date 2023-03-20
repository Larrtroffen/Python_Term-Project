# 大写字母变成对应的小写字母输出
# 方法一：
S = input('请输入：')
print(S.lower())

# 方法二：
S = input('请输入：')
s = ''
for j in S:
    if j >= 'A' and j <= 'Z':
        s += chr(ord(j) + ord('a') - ord('A'))
    else:
        s += j
print(s)

