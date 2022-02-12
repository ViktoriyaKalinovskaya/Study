import random

a = 0
b = 0
i = 1
while i <= 6:
    num1 = int(input('Введите первое число от 1 до 20: '))
    num2 = int(input('Введите второе число от 1 до 20: '))
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    if num1 > n1 and num2 > n2:
        a += 1
    else:
        b += 1
    i += 1
    if a == b and i == 4:
        print(num1, num2, '\n', n1, n2)
print(a)
