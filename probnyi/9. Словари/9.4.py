Words = dict()
count = int(input('Количество слов в словаре: '))
i = 0
while i < count:
    print('Ввод слов')
    wrd = input('Слово: ')
    value = int(input('Значение: '))
    if wrd not in Words:
        Words[wrd] = value
    i = i + 1
print(Words)
