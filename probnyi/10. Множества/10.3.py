# a = [1, 5, 3, 5, 1]
# b = set(a)
# print(len(a)==len(b))

a = {1, 5, 3, 5, 1}
b = frozenset([7, 5, 4, 6, 3])
# print(a | b)
print(a & b)
