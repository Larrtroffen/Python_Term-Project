strs = "Can you can a can as a Canner can can a can."
cnt = 0
for char in strs:
    if ord(char) == 67 or ord(char) == 99:
        cnt+=1

print(cnt)