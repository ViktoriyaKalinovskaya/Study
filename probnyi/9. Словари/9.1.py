# a = {}
# d = {'dict': 1, 'dictionaty': 2}
# print(d)

# d = dict(short='dict', long='dictionary')
# d_2 = dict([(1,1), (2, 4)])
# print(d, '\n', d_2)

# d = dict.fromkeys(['a', 'b'])
# d_2 = dict.fromkeys(['a', 'b'], 100)
# print(d, '\n', d_2)

# d = {a: a ** 2 for a in range(7)}
# print(d)

# d = {1: 2, 2: 4, 3: 9}
# d[4] = 4 ** 2
# print(d[1])
# print(d)

# Months = { 1:'Jan', 2:'Feb', 3:'Mar',
#            4:'Apr', 5:'May', 6:'Jun',
#            7:'Jul', 8:'Aug', 9:'Sep',
#            10:'Oct', 11:'Nov', 12:'Dec' }
# count = len(Months)
# print(count)

# Salary = {'Director': 120800.0,
#           'Secretary': 101150.25,
#           'Locksmith': 188200.00}
# print(Salary)
# # Удалить элемент по ключу 'Secretary'
# del Salary['Secretary']
# print(Salary)
# # Попытка удалить несуществующий ключ
# # del Salary[5] - так нельзя, генерируется исключение KeyError: 5
# # del Salary['None'] - тоже запрещенно

# Numbers = dict(zip([1, 2, 3], ['One', 'Two', 'Three']))
# print(Numbers)