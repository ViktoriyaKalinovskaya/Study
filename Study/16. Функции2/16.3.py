# def razriad(x): print(len(x))
# razriad(input('Введите число: '))

a = []
b = []
def fun(*args, **kwargs):
    for i in args:
        if args.index(i) % 2 == 0:
            a.append(i)
    for j in kwargs.values():
        if type(j) is str:
            b.append(j)
    return a, b
print(fun(4, 8, 23, 17, 9, animals='dog, cat', fruits='apple', num=[1, 2, 3]))
