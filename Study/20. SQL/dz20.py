import sqlite3
class Baza_dannych:
    def baza(self):
        conn = sqlite3.connect('baza.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS arg(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
