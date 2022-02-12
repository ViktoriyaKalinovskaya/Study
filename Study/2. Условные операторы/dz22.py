day = int(input('Введите день Вашего рождения: '))
month = int(input('Введите месяц Вашего рождения: '))
year = int(input('Введите год Вашего рождения: '))

dayNow = int(input('Введите сегодняшний день: '))
monthNow = int(input('Введите сегодняшний месяц: '))
yearNow = int(input('Введите сегодняшний год: '))

if monthNow - month <= 0 and day <= dayNow:
    print(yearNow - year - 1, 'year')
elif monthNow - month >= 0 and dayNow > day:
    print(yearNow - year, 'year')

if 23 <= day <= 31 and month == 12 or 1 <= day <= 20 and month == 1:
    print('Козерог')
elif 21 <= day <= 31 and month == 1 or 1 <= day <= 19 and month == 2:
    print('Водолей')
elif 20 <= day <= 31 and month == 2 or 1 <= day <= 20 and month == 3:
    print('Рыбы')
elif 21 <= day <= 31 and month == 3 or 1 <= day <= 20 and month == 4:
    print('Овен')
elif 21 <= day <= 31 and month == 4 or 1 <= day <= 21 and month == 5:
    print('Телец')
elif 22 <= day <= 31 and month == 5 or 1 <= day <= 21 and month == 6:
    print('Близнецы')
elif 22 <= day <= 31 and month == 6 or 1 <= day <= 22 and month == 7:
    print('Рак')
elif 23 <= day <= 31 and month == 7 or 1 <= day <= 21 and month == 8:
    print('Лев')
elif 22 <= day <= 31 and month == 8 or 1 <= day <= 23 and month == 9:
    print('Дева')
elif 24 <= day <= 31 and month == 9 or 1 <= day <= 23 and month == 10:
    print('Весы')
elif 24 <= day <= 31 and month == 10 or 1 <= day <= 22 and month == 11:
    print('Скорпион')
elif 23 <= day <= 31 and month == 11 or 1 <= day <= 22 and month == 12:
    print('Стрелец')
