import sqlite3
import random
con = sqlite3.connect('name_dz.db')
cursor0 = con.cursor()
cursor0.execute('''CREATE TABLE IF NOT EXISTS tablica0(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,col_2 INTEGER)''')
for i in range(3):
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    cursor0.execute('''INSERT INTO tablica0(col_1, col_2) VALUES(?,?)''',(x,y))
# con.commit()
cursor0.execute('''SELECT col_1, col_2 FROM tablica0''')
k = cursor0.fetchall()
print(k)
s = 0
for i in k:
    for j in i:
        s += j
print('SUM', s)
ar = (s/(len(k)*2))
print('AR', ar)
if ar > len(k):
    cursor0.execute('''DELETE FROM tablica0 WHERE id = 4''')
# con.commit()
cursor0.execute('''SELECT * FROM tablica0''')
k = cursor0.fetchall()
print(k)