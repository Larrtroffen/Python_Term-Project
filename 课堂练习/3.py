def is_ascending(name):
    a = 0
    for i in name:
        if ord(i) > a:
            continue
        else:
            break
    return True
name1 = input()
print(is_ascending(name1))