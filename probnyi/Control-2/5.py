Magazin = {'Брауни': ['сливочное масло, тёмный шоколад, мука, яйца, сахарная пудра,какао, соль', 8.90, 900],
           'Панкейки': ['кефир, яйцо, сахар, мука, сода, разрыхлитель, соль', 1.90, 550],
           'Щербет с арахисом': ['молоко, сахар, арахис, масло сливочное', 1.20, 1500],
           'Макаруны': ['мука миндальная, сахарная пудра, яичный белок, сахар, вода, шоколад белый, сливки, малина, кофе растворимый', 8, 2000]}
Summa = []
while True:
    Ch = input('Выберите опцию - состав, цена(100гр), количество, вся информация: ')
    for key in Magazin:
        if Ch == 'состав':
            print(key, '-', Magazin[key][0])
        elif Ch == 'цена':
            print(key, '-', Magazin[key][1])
        elif Ch == 'количество':
            print(key, '-', Magazin[key][2])
        elif Ch == 'вся информация':
            print(key, '-', Magazin[key][0], '-', Magazin[key][1], '-', Magazin[key][2])
        elif Ch == '':
            Art = input('Выберите продукт: ')
            if Art == 'n':
                break
            Amt = int(input('Введите количество желаемого продукта (гр): '))
            for i in Magazin:
                if Art == i:
                    Summa.append((Amt / 100) * Magazin[Art][1])
                    Magazin[Art][2] = Magazin[Art][2] - Amt
    if Ch == 'n':
        break
print('Сумма в корзине:', sum(Summa))
for key in Magazin:
    print(key, '-', Magazin[key][2])
print('До свидания!')
