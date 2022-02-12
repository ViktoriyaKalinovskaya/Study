a = input('Введите строку: ')
big = ''
small = ''
low = 0
up = 0
for i in a:
    if i.islower():
        small += i
        if len(small) % 2 == 0:
            low += 1
    elif small != '':
        small = ''
    if i.isupper():
        big += i
        if len(big) % 2 == 0:
            up += 1
    elif big != '':
        big = ''
print('Пары нижнего регистра -', low, 'Пары верхнего регистра -', up)
gl = 0
ngl = 0
b = 'aeiouyAEIOUY'
for i in a:
    if i.isalpha():
        if i in b:
            gl += 1
        else:
            ngl += 1
print('Всего букв:', gl + ngl)
print('Количество гласных:', gl)
print('Количество согласных:', ngl)
