# a = int(input())
# b = int(input())
# c = int(input())
# if a > 0 and b < 0:
#     print('and')
# elif a > 0 or b < 0:
#     print('or')
#
# if not(c > 0) == True:
#     print('not')
#

# a = int(input())
# b = int(input())
# c = int(input())
# if a>b and a>c:
#     print('Наибольшее число первое')
# elif c>a and c>b:
#     print('Наибольшее число третье')
# else:
#     print('Наибольшее число второе')

a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    print('Наибольшее число первое')
else:
    if b>c:
        print('Наибольшее число второе')
    else:
        print('Наибольшее число третье')
