def card_number():
    a = input('Введите номер кредитной карты: ')
    b = a[:len(a) - 4]
    c = a[len(a) - 4:len(a) + 1]
    for i in b:
        if i == ' ': continue
        b = b.replace(i, '*')
    print(b + c)

card_number()
