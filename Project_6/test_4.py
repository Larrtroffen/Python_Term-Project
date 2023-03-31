# 确定输入不同字符的数量
def cstr(my_s):
    my_set = set()
    for char in my_s:
        if char not in my_set:
            my_set.add(char)
        else:
            continue
    return len(my_set)

if __name__== "__main__" :
    my_s = 'Hello,World!'
    print(cstr(my_s))