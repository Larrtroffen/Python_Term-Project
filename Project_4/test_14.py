# 练习14
def date_format(str):
    year , month , day = str.split('/')
    return f"{year}年{month}月{day}日"
    
str = input("请以“xxxx/xx/xx”的格式输入一个日期")
print(date_format(str))