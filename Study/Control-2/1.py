s = input('Введите строку: ')
sp = []
for i in s:
    sp.append(i)
for j in sp:
    if j == ' ':
        continue
    elif sp.count(j) == 1:
        print(j)
