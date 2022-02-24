import sqlite3
con = sqlite3.connect('movie.db')
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(movie_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, release_year INTEGER, genre TEXT)''')
# con.commit()
def add_movie():
    name = input('Введите название фильма: ')
    release_year = int(input('Введите год выхода фильма: '))
    genre = input('Введите жанр фильма: ')
    cursor.execute('''INSERT INTO movies(name, release_year, genre) VALUES (?,?,?)''',(name, release_year, genre))
    con.commit()
def all_info():
    cursor.execute('''SELECT*FROM movies''')
    k = cursor.fetchall()
    print(k)
    con.commit()
def one_info():
    d = input('Введите номер фильма для получения информации: ')
    cursor.execute('''SELECT * FROM movies WHERE movie_id=?''',(d,))
    k = cursor.fetchall()
    print(k)

while True:
    func = input('Выберите опцию(add, all_info, one_info, exit): ')
    if func == 'add':
        add_movie()
    elif func == 'all_info':
        all_info()
    elif func == 'one_info':
        one_info()
    elif func == 'exit':
        break

