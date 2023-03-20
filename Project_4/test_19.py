strs = "Hello Lvye!"
lst = list(strs)
new_str = ""
for char in lst:
    if char != 'e':
        new_str+=char
print(new_str)