# 练习5
message = input("请输入消息:")
num = int(input("请输入移位量:"))
new_message = ""
for char in message:
# 判断是否为字母，如果是字母再进行位移
    if char.isalpha():
# 判断大小写，使用ord使字母变成对应的编码
        if char.isupper():
            new_message += chr((ord(char) + num - 65) % 26 + 65)
        else:
            new_message += chr((ord(char) + num - 97) % 26 + 97)
    else:
        new_message += char
print(new_message)