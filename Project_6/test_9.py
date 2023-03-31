IEEE_set = set(['Python','C++','C','Java','C#'])
TIOBE_set = set(['Python','C++','C','Java','VB.NET'])

print(IEEE_set.union(TIOBE_set))
print(IEEE_set.intersection(TIOBE_set))
print(IEEE_set)
print(IEEE_set.union(TIOBE_set).difference(IEEE_set.intersection(TIOBE_set)))