import sqlite3
import random
con = sqlite3.connect('simple.db')
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_25(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,col_2 INTEGER)''')
for i in range(3):
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    cursor.execute('''INSERT INTO tab_25(col_1, col_2) VALUES(?,?)''',(x,y))
# con.commit()
cursor.execute('''SELECT col_1, col_2 FROM tab_25''')
k = cursor.fetchall()
print(k)

cursor.execute('''SELECT id FROM tab_25''')
nId = cursor.fetchall()
print(nId)
r = random.choice(nId)
# print(*r) # * используется для распаковки элемента из кортежа
cursor.execute('''SELECT col_1,col_2 FROM tab_25 WHERE id=?''', (r))
zapis = cursor.fetchall()
print(zapis)
if zapis[0][0] % 2 == 0 and zapis[0][1] % 2 == 0:
    cursor.execute('''DELETE FROM tab_25 WHERE id = ?''',(r))
else:
    cursor.execute('''UPDATE tab_25 SET col_1='2', col_2='2' WHERE id = ?''',(r))
con.commit()
cursor.execute('''SELECT * FROM tab_25''')
k = cursor.fetchall()
print(k)
