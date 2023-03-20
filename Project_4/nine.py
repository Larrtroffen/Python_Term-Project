# 字符串的开头和结尾变成’-’
s = input('请输入：')
str = []
for i in range(len(s)):
    if ((i == 0) or (i == len(s) - 1)):
        str += '+'
        continue
    str += s[i]
print(''.join(str))
