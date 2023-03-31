# 练习2
def output(str1):
    str1 = str1.upper()
    result = ''
    for letter in str1:
        i = str(mapping(letter))
        result += i
    return result

def mapping(letter):
    dict = {0:' ',1:'.,?!:',2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PQRS',8:'TUV',9:'WXYZ'}
    for i in dict:
        if letter in dict[i]:
            j = dict[i].index(letter)+1
            return str(i)*j

str1 = str(input('请输入字符串'))
print(output(str1))
