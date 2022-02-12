import random
b = int(input('Введите камень(1), ножницы(2) или бумага(3): '))
a = random.randint(1, 3)
print(b)
if a == b:
    print('ничья')
elif a == 1 and b == 2:
    print('Вы проиграли')
elif a == 2 and b == 1:
    print('Вы выиграли')
elif a == 1 and b == 3:
    print('Вы выиграли')
elif a == 3 and b == 1:
    print('Вы проиграли')
elif a == 2 and b == 3:
    print('Вы проиграли')
elif a == 3 and b == 2:
    print('Вы выиграли')
