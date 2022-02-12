Magazin = {'Яблоки': [3, 15],
           'Бананы': [2, 5],
           'Апельсины': [4, 24],
           'Киви': [6, 20]}
for key in Magazin:
    print(key, '-', Magazin[key][0], '-', Magazin[key][1])
Summa = []
while True:
    Art = input('Выберите продукт: ')
    if Art == '0':
        break
    Amt = int(input('Введите количество желаемого продукта: '))
    for i in Magazin:
        if Art == i:
            Summa.append(Amt * Magazin[Art][0])
            Magazin[Art][1] = Magazin[Art][1] - Amt
print('Сумма в корзине:', sum(Summa))
for key in Magazin:
    print(key, '-', Magazin[key][0], '-', Magazin[key][1])
