with open('Class.txt', encoding='utf-8') as f:
    s = list(f.readlines())
mean = []
a = 0
clas = []
for i in s:
    i = i.replace('\n', '')
    for j in i:
        if j.isdigit():
            mean.append(int(j))
            a += 1
            if int(j) < 3:
                clas.append(i)
                i = i.replace('\n', '')
print(s)
print(clas)
print('Среднее значение - ', sum(mean) / a)


