a = '1a23$3k 1999);gd13'
b = ''
arr = []
for i in a:
    if i.isdigit():
        b += i
    elif b != '':
        arr.append(b)
        b = ''
if b != '':
    arr.append(b)
print(', '.join(arr))