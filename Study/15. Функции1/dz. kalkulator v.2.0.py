num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
def plus(a, b): return print(a + b)
def minus(a, b): return print(a - b)
def umnoz(a, b): return print(a * b)
def delit(a, b): return print(a / b)
while True:
    operation = input('Введите знак: ')
    if operation == '0': break
    elif operation == '+': plus(num1, num2)
    elif operation == '-': minus(num1, num2)
    elif operation == '*': umnoz(num1, num2)
    elif operation == '/':
        try:
            delit(num1, num2)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
        else:
            delit(num1, num2)
