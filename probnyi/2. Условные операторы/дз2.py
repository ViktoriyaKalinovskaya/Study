import random

numb = int(input('Введите число от 0 до 2000: '))
numb1 = random.randint(0, 2000)
if numb == numb1:
    print('Вы выиграли')
else:
    print('Вы проиграли')
