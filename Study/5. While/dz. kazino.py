import random
c1 = 'красный'
c2 = 'чёрный'
i = 5
print('Добро пожаловать в казино!')
while 0 <= i <= 5:
    n = random.randint(1, 10)
    c = random.randint(1, 2)
    if i == 5:
        print('У Вас есть', i, 'попыток')
    elif i == 1:
        print('У Вас осталась', i, 'попытка')
    elif i == 0:
        print('Закончились попытки(')
        break
    else:
        print('У Вас осталось', i, 'попытки')
    numb = int(input('Введите число - '))
    if numb == 0:
        break
    color = input('Введите цвет - ')
    if numb != n and color != c:
        print('Вы проиграли(')
        print('Правильная комбинация -', n, c)
        i -= 1
    elif numb != n and color != c:
        print('Вы проиграли(')
        print('Правильная комбинация -', n, c)
        i -= 1
    elif numb != n and color == c:
        print('Вы проиграли(')
        print('Правильная комбинация -', n, c)
        i -= 1
    elif numb == n and color != c:
        print('Вы проиграли(')
        print('Правильная комбинация -', n, c)
        i -= 1
    elif numb == n and color == c:
        print('Вы выиграли!')
        i = 5
