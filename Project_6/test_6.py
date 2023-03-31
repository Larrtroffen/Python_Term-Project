strs1 = input("请输入第一个字符串：")
strs2 = input("请输入第二个字符串：")

def create_dict(strs:str):
    char_dict = {}
    strs = strs.lower()
    for char in strs:
        if char.isalpha():
            char_dict[char] = strs.count(char)
    return char_dict

dict1 = create_dict(strs1)
dict2 = create_dict(strs2)

if strs1 != strs2 and dict1 == dict2:
    print('是字谜')
else:
    print("不是字谜")