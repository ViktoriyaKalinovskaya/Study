s = input('Введите числа через пробел: ')
s = s.split()
st = set(s)
par1 = 0
par2 = 0
for i in st:
    if s.count(i) % 2 == 0:
        par1 += s.count(i)/2
    elif s.count(i) % 2 != 0:
        par2 += (s.count(i) - 1)/2
print('Количество пар в строке:', par1 + par2)
