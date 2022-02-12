# Person = {'name': 'Victoria',
#           'age': 21,
#           'city': 'Mogilev'}
# print(Person['age'])

# Mach = {'BMW': [1, 2, 3],
#         'Tesla': [1, 2, 3]}
# print(Mach['BMW'][0], ',', Mach['BMW'][2], '\n',
#       Mach['Tesla'][0], ',', Mach['Tesla'][2])

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# print(d1['b'] == d2['b'])

dict = {1: 2, 2: 5, 3: 11}
pr = 1
for i in dict:
    pr *= dict[i]
print(pr)
