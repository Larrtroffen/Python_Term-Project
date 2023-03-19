# 练习14
def date_format(str):
    str_list = str.split('/')
    format_date = str_list[0]+'年'+str_list[1]+'月'+str_list[2]+'日'
    return format_date
    
str = input("请以“xxxx/xx/xx”的格式输入一个日期")
print(date_format(str))