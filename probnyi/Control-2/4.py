s = 'An apple a day keeps the doctor away'
s = s.replace(' ', '')
d = {i: s.count(i) for i in s}
print(d)
