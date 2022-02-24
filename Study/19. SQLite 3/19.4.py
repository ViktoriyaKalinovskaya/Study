import sqlite3

con = sqlite3.connect('types.db')
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book(book_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(50), author VARCHAR(30), price DECIMAL(8, 2), amount INTEGER)''')
# con.commit()
title = input('Введите название: ')
author = input('Введите автора: ')
price = input('Введите цену: ')
amount = input('Введите количество: ')
cursor.execute('''INSERT INTO book(title, author, price, amount) VALUES (?,?,?,?)''', (title, author, price, amount))
cursor.execute('''SELECT*FROM book''')
k = cursor.fetchall()
print(k)