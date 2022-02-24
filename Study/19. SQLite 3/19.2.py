import sqlite3
baza = sqlite3.connect('tablica2.db')
cursor = baza.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(col_1 TEXT,col_2 TEXT,col_3 INT)''')
# num = input('Введите число: ')
# cursor.execute('''INSERT INTO tab_2(col_1, col_2, col_3) VALUES('Hello','World',?)''',(num,))
# baza.commit()

cursor.execute('''SELECT*FROM tab_2''')
k = cursor.fetchall()
for i in k:
    e = 0
    h = list(i)
    m = ' '.join(str(e) for e in h)
    print(m)
