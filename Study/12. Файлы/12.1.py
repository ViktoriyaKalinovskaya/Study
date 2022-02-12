# f = open('example.txt', 'r') # открыть файл из рабочей директории в режиме чтения
# fp = open('D:/blok.txt', 'r') # открыть файл из любого каталога
# print(*fp)
# print(fp)
# fp.close() # закрыть файл

# f = open('example.txt', 'r', encoding='utf-8') # открыть файл с русскими символами в файле

# fp = open('D:/blok.txt', 'r')
# try:
#     print(*fp)
# finally:
#     fp.close()

# with open('D:/blok.txt') as fp:
#     print(*fp)

# f = open('D:/blok.txt')
# print(f.read(7))

# f = open('D:/blok.txt', 'r')
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# f = open('xyz.txt', 'w') # открытие в режиме записи
# f.write('Hello \nWorld') # запись Hello World В файл
# f.close() # закрытие файла
