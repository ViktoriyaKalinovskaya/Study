# def a_function():
#     print('You just created a function!')
# a_function()

# def empty_function():
#     pass

# s = [1, 2, 3, 4, 5]
# def numbS():
#     print(sum(s))
# numbS()

# def add(a, b):
#     return a + b
# print(add(1, 2)) # 3
# print(add(a=2, b=3))
# total = add(b=4, a=5)
# print(total)

# def keyword_function(a=1, b=2):
#     return a + b
# print(keyword_function(b=4, a=5))
# print(keyword_function())

# def mixed_function(a, b=2, c=3):
#     return a + b + c
# # print(mixed_function(b=4, c=5)) # пропустили "а", сколько аргументов столько и значений
# print(mixed_function(1, b=4, c=5))
# print(mixed_function(1)) # 1+2+3=6, для "а"-1, остальные прописаны вначале

# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)
# many(1, 2, 3, name='Mike', job='programmer')

# def function_a():
#     global a
#     a = 1
#     b = 2
#     return a + b
# def function_b():
#     c = 3
#     return a + c
# print(function_a())
# print(function_b())
