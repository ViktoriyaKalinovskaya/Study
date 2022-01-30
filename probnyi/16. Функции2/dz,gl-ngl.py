def schet_gl_ngl(a):
    gl = 0
    ngl = 0
    b = 'aeiouyаоэеиыуёюяAEIOUYАЕЁИОУЫЭЮЯ'
    for i in a:
        if i in ' ': continue
        elif i in b: gl += 1
        else: ngl += 1
    print('Количество гласных -', gl,' ','Количество согласных -', ngl)
s = input('Введите строку: ')
schet_gl_ngl(s)
