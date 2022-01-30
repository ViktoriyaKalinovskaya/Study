# import random
# a = tuple(random.randint(1, 100) for i in range(10))
# print('max:', max(a), 'min:', min(a))

# a = tuple(int(random.randint(0, 5)) for i in range(10))
# b = tuple(int(random.randint(-5, 0)) for t in range(10))
# c = a + b
# print(c)
# print('Количество нулей:', c.count(0))

# a = ('1', '2', '3', '4', '5')
# c = ','.join(a)
# # c = ','.join([str(i) for i in a]) # преобразование цифр в строки для картежа
# print(c)

# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# if sum(A)>sum(B):
#     print('Сумма больше в кортеже - A')
# else:
#     print('Сумма больше в кортеже - B')
# print('Порядковый номер кортежа А:', A.index(min(A))+1)
# print('Порядковый номер кортежа В:', B.index(min(B))+1)
