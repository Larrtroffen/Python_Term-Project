str1 = str(input()).lower()
dic = {}
for i in str1:
    dic[i]=str1.count(i)
for key in dic:
    print(key)
    print(dic[key])
    
    