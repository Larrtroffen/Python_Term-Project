
def vowels_count(str):
    count = 0
    for i in str:
        if i == 'a' or 'e' or 'i' or 'u' or 'o' or 'A' or 'E' or 'I' or 'O' or 'U':
            count += 1
        else:
            continue
    return count

str1 = str(input())

print(vowels_count(str1))