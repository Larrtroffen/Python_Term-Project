# 反向查找
def reverseLookup(my_dict,mvalue):
    ls = []
    for key in my_dict:
        if my_dict[key] == mvalue:
            ls.append(key)
    return ls

if __name__== "__main__" :
    my_dict = {'1':'2', '2':'2', '3':'3', '4':'4'}
    mvalue = '2'
    print(reverseLookup(my_dict,mvalue))