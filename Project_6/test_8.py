# 练习8
nations = {'China':'Chinese','USA':'English','France':'French','Germany':'German'}

def all_keys(dic):
    result = []
    for key in dic:
        result.append(key)
    return result

def all_items(dic):
    result = []
    for key in dic:
        result.append((key,dic[key]))
    return result

def all_dict(dic):
    result = {}
    for key in dic:
        result[dic[key]] = key
    return result

def france(dic):
    if 'France' in dic:
        return dic['France']
    else:
        return 'Not Found'
    
def update():
    new_dict = {'Spain':'Spanish','Japan':'Japanese'}
    nations.update(new_dict)
    
if __name__== "__main__" :    
    print(all_keys(nations)) # 显示字典的所有键
    print(all_items(nations)) # 显示字典的所有值
    print(all_dict(nations)) # 显示字典的所有项
    print(france(nations)) # 获取键'France'对应得值
    update() # 更新字典
    print(nations) # 显示更新后的字典
