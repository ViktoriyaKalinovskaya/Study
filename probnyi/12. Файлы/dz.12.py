file = open('file.txt', 'w')
while True:
    f = input('Введите строку: ')
    file.write(f)
    if f == '':
        break
    file.write('\n')
file.close()
with open('file.txt') as f:
    print(f.read())
