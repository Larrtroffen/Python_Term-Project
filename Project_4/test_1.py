strs = input("请输入一个字符串：")
new_strs = [ char for i,char in enumerate(strs) if i%2 == 0]
print(''.join(new_strs))