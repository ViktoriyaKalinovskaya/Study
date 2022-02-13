def polindrom():
    s = input('Введите слово: ')
    s1 = s[::-1]
    if s == s1:
        print('Слово является палиндромом')
    else:
        print('Слово не является палиндромом')

polindrom()