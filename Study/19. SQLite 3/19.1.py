import sqlite3

# Создаем базу данных
conn = sqlite3.connect('name.db')
# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
cursor = conn.cursor()
# Создаем таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT)''')

# Заполняем таблицу данными
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES('hello','world')''')
d = 'red'
f = 'black'
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES(?,?)''',(d,f))
# # Сохраняем изменения
# conn.commit()

# Запросить данные
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)


# # EXAMPLE!!!!
# # Вытакже можете использовать функцию fetchone() для получения первого результата
# a = 'hello'
# cursor.execute('''SELECT * FROM tab_1 where col_1='hello' ''')
# conn.commit()
# k = cursor.fetchall()
# print(k)
#
# # Список всех записей отсортированных относительно третьей колонки
# cursor.execute('''SELECT * FROM tab_1 ORDER BY col_3''')
# conn.commit()
# k = cursor.fetchall()
# print(k)
#
# # Внашем случае, мы искали по всей таблице записи третьей колонки, которые начинаются с 7.
# # Знак процента (%) является подстановочным оператором.
# cursor.execute('''SELECT * FROM tab_1 WHERE col_3 LIKE '7%' ''')
# conn.commit()
# k = cursor.fetchall()
# print(k)


# Удаление записи из таблицы по id, по значению
# cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
# conn.commit()
# cursor.execute('''DELETE FROM tab_1 WHERE col_1='red' ''')
# conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)

# Обновление данных в таблице
t = 5
cursor.execute('''UPDATE tab_1 SET col_1='world' WHERE id=?''', (t,))
# conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
