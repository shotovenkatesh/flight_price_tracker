languages = ['Python', 'C', 'C++', 'C#', 'Java']


d1 = None
d2 = None

for i,language in enumerate(languages):
    if i == 0:
        d1 = language
    if i == 1:
        d2 =language

data = (d1,d2)
print(d1,d2)
