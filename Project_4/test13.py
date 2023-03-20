strs = input("请输入您的名字：")
if strs.find("hello")!=-1:
    new_strs=strs.replace("hello", "*")
    print(new_strs)