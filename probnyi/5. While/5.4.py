# простой калькулятор через While
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
while True:
    operation = input('Введите знак: ')
    if operation == '0':
        break
    elif operation == '+':
        print(num1+num2)
    elif operation == '/':
        if num2 != 0:
            print(num1 / num2)
        else:
            print('Ошибка')
    elif operation == '-':
        print(num1-num2)
    elif operation == '*':
        print(num1*num2)
