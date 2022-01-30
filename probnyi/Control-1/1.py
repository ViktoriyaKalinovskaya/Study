num = input('Введите 7-значное число: ')
chet = 0
niechet = 0
sum = 0
pr = 1
for i in num:
    if int(i) % 2 == 0:
        chet += 1
    else:
        niechet += 1
if chet > niechet:
    for i in num:
        sum += int(i)
    print('Сумма', sum)
else:
    pr = int(num[0])*int(num[2])*int(num[5])
    print('Произвидение', pr)

