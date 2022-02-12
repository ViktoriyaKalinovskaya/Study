# arr = ['бекон', 'яичница', 'оладки', 'борщ', 'пельмени']
# print(arr)
# a = input('Название блюда: ')
# for i in arr:
#     if i == a:
#         print('Я не ем', a)

arr = [1, 2, 3]
sum = 0
sub = 1
for i in arr:
    sum += i
    sub *= i
print(sum)
print(sub)