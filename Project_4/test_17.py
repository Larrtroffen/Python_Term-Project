# 练习17
def split(str):
    str_list = str.split()
    return str_list

str = input('请输入字符串\n')
print(*split(str),sep='\n')
