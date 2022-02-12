list = [15, 48, 'hello', 6, 19, 'world']
glasnye = 0
soglasnye = 0
sum = 0
print(list)
for i in list:
    if type(i) == int and i % 2 == 0:
        sum += i
    elif type(i) == int and i % 2 != 0:
        a = list.index(i)
        list[a] = 1
print(list)
print('Сумма четных чисел -', sum)

for i in list:
    if type(i) == str:
        for s in i:
            if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'y':
                glasnye += 1
            else:
                soglasnye += 1
print('glasnye -', glasnye)
print('soglasnye -', soglasnye)
