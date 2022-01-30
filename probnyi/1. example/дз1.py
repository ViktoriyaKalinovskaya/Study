import random

numb = random.randint(100, 999)
s1 = numb // 100
s2 = (numb // 10) % 10
s3 = numb % 10
print(numb)
print(s1, ',', s2, ',', s3)
S = s1 + s2 + s3
print('Сумма=', S)
