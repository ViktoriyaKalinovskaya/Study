# a = [1, 3, 5]
# b = [1, 5, 8, 9]
# print(a + b)

# d = ['h', 'e', 'l', 'l', 'o']
# e = ['w', 'o', 'r', 'l', 'd']
# d.extend(e) # extend не возвращает новый список, а дополняет текущий
# print(d)

# a = ['cat', 'elephant', 'snake']
# b = a.copy() # нужный способ
# print(a, b)

# d = list(a) # нужный способ
# print(a, d)
#
# import copy
# e = copy.copy(a) # устаревший способ
# print(a, e)
#
# f = copy.deepcopy(a) # устаревший способ
# print(a, f)
#
# c = a[:] # устаревший способ копирования через срезы
# print(a, c)

a = [1, 2, 3, 4, 5, 6, 7, 8]
e = a[0:8:2] # устаревший способ копирования через срезы
print(e)
