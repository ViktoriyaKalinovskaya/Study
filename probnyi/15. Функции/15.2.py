# def func1(a, b):
#     def inner_func(x):
#         return x * x * x
#     return inner_func(a) + inner_func(b)
# print(func1(4, 5))

# def sum(a, b): return a + b
# print(sum(1, 5))

# def is_year_leap(a): return a%4==0 or a%400==0 and a%100!=0
# print(is_year_leap(2022))

# import math
# def square(a): return 4*a, a**2, a*math.sqrt(2)
# print(square(int(input('Введите число: '))))

def season(a):
    if 1<=a<=2 or a == 12: print('Зима')
    elif 3<=a<=5: print('Весна')
    elif 6<=a<=8: print('Лето')
    elif 9<=a<=11: print('Осень')
    else: print('Такого месяца нет')
print(season(int(input('Введите номер месяца: '))))
