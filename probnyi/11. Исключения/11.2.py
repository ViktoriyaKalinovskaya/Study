# a = 100 / 0

# try:
#     k = 1 / 0
# except ZeroDivisionError:
#     k = 0
#     print(k)

# try:
#     k = 1 / 0
# except ArithmeticError:
#     k = 0
# print(k)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Кюча не существует!')

# my_list = [1, 2, 3, 4, 5]
# try:
#     my_list[6]
# except IndexError:
#     print('Этого индекса нет в списке!')

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Кюча не существует!')
# except IndexError:
#     print('Этого индекса нет в списке!')
# except:
#     print('Произошла другая ошибка!')

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['d']
# except (KeyError, IndexError):
#     print('Произошла ошибка KeyError или IndexError!')

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Произошла ошибка KeyError')
# finally:
#     print('Оператор finally выполнен!')

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Произошла ошибка KeyError')
# else:
#     print('Ошибок не произошло!')

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('Произошла ошибка KeyError')
# else:
#     print('Ошибок не произошло!')
# finally:
#     print('Оператор finally выполнен!')

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# try:
#     f = num1 / num2
# except ZeroDivisionError:
#     print('Произошла ошибка ZeroDivisionError')
# else:
#     print(f ** 2)
# finally:
#     print('Оператор finally выполнен!')

