s = 'Новый год - это праздник, который пришел из сказки!'
y = ''
ss = []
for i in s:
    if i.isalpha():
        y += i
    elif y != '':
        ss.append(y)
        y = ''
ss = tuple(ss)
print(ss)
print('Самое длинное слово:', max(ss, key=len))
