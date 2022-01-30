file = open('abc.txt')
bfile = file.readline()
file.close()
bfile = bfile.replace('_', ' ')
bfile = bfile.split()
nfile = []
for i in bfile:
    if i.isdigit():
        i = int(i)
        nfile.append(i)
print(sum(nfile))

# это к домашнему заданию
# import os
# os.remove('file.txt')