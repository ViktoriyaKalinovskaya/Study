num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
try:
    f = num1 / num2
except ZeroDivisionError:
    print('Произошла ошибка ZeroDivisionError')
finally:
    print('Оператор finally выполнен!')
