import random
a = int(input('Количество чисел: '))
b = input('Искомая цифра: ')
c = 0
numbs = [random.randint(100, 1500) for i in range(a)]
numb = str(numbs)
for i in numb:
    if b in i:
        c += 1
print('Количество искомой цифры:', c)
print(numb)
