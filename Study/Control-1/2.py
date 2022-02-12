a = input('Введите фразу на английском: ')
gl = 0
ngl = 0
b = 'aeiouy'
frGl = []
for i in a:
    if i in ' ':
        continue
    elif i in b:
        frGl.append(i)
        gl += 1
    else:
        ngl += 1
print('Количество гласных:', gl)
print('Количество согласных:', ngl)
if gl == ngl:
    print('Гласные находящиеся во фразе:', ','.join(frGl))
