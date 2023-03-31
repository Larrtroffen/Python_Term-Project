# IEEE & TIOBE
IEEE = {'Python', 'C++', 'C', 'Java', 'C#'}
TIOBE = {'Java', 'C', 'Python', 'C++', 'VB.NET'}
TOTAL = IEEE | TIOBE
print(TOTAL)
SAME = IEEE & TIOBE
print(SAME)
print(IEEE)
print((IEEE-TIOBE), (TIOBE-IEEE))